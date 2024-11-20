import pandas as pd
import ast
import asyncio
import aiohttp
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Function to extract city and coordinates
def extract_address_details(address):
    try:
        address_dict = ast.literal_eval(address)  # Convert string to dictionary
        city = address_dict.get('city', None)
        coordinates = address_dict.get('coordinates', None)
        return city, coordinates
    except (ValueError, SyntaxError):
        return None, None

def extract_location_details(location):
    try:
        if isinstance(location, str):
            location_dict = ast.literal_eval(location)  # Convert string to dictionary
        else:
            location_dict = location
        latitude = location_dict.get('lat', 0.0)
        longitude = location_dict.get('lng', 0.0)
        return latitude, longitude
    except (ValueError, SyntaxError, AttributeError):
        return 0.0, 0.0

# Transformation function for weather data
def transformation_data(weather_data):
    return {
        "temperature": weather_data.get("current_weather", {}).get("temperature", "N/A"),
        "windspeed": weather_data.get("current_weather", {}).get("windspeed", "N/A"),
        "time": weather_data.get("current_weather", {}).get("time", "N/A"),
    }

# Asynchronous function to fetch weather data
async def fetch_weather_data(session, latitude, longitude, row_id):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true"
        }
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                transformed_data = transformation_data(data)
                transformed_data["id"] = row_id  # Include the row ID for mapping
                return transformed_data
            else:
                print(f"Error: {response.status}, {await response.text()}")
                return {"id": row_id, "temperature": "N/A", "windspeed": "N/A", "time": "N/A"}
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return {"id": row_id, "temperature": "N/A", "windspeed": "N/A", "time": "N/A"}

# Asynchronous function to process all rows
async def process_data(data):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for index, row in data.iterrows():
            latitude = row['latitude']
            longitude = row['longitude']
            row_id = row['id']  # Track the row ID
            if latitude != 0.0 and longitude != 0.0:  # Only process valid coordinates
                tasks.append(fetch_weather_data(session, latitude, longitude, row_id))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

# Task 1: Load CSV
def load_csv(**kwargs):
    data = pd.read_csv("data_file.csv")
    kwargs['ti'].xcom_push(key='raw_data', value=data.to_dict(orient='records'))

# Task 2: Extract details
def extract_details(**kwargs):
    data = pd.DataFrame(kwargs['ti'].xcom_pull(key='raw_data'))
    data[['city', 'location']] = data['address'].apply(
        lambda x: pd.Series(extract_address_details(x))
    )
    data[['latitude', 'longitude']] = data['location'].apply(
        lambda x: pd.Series(extract_location_details(x))
    )
    data = data.drop(columns=['address', 'location'])
    kwargs['ti'].xcom_push(key='processed_data', value=data.to_dict(orient='records'))

# Task 3: Fetch weather data
def fetch_weather_data_task(**kwargs):
    data = pd.DataFrame(kwargs['ti'].xcom_pull(key='processed_data'))
    results = asyncio.run(process_data(data))
    weather_data = pd.DataFrame(results)
    kwargs['ti'].xcom_push(key='weather_data', value=weather_data.to_dict(orient='records'))

# Task 4: Merge results
def merge_and_save_results(**kwargs):
    data = pd.DataFrame(kwargs['ti'].xcom_pull(key='processed_data'))
    weather_data = pd.DataFrame(kwargs['ti'].xcom_pull(key='weather_data'))
    final_data = data.merge(weather_data, on="id", how="left")
    final_data.to_csv("updated_data.csv", index=False)

# Define DAG and tasks
default_args = {
    'owner': 'enes',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'etl_employee_weather',
    default_args=default_args,
    description='ETL pipeline to fetch, transform, and load weather data',
    schedule_interval='@hourly',
    catchup=False,
    start_date=datetime(2024, 11, 20),
)

load_csv_task = PythonOperator(
    task_id='load_csv',
    python_callable=load_csv,
    provide_context=True,
    dag=dag,
)

extract_details_task = PythonOperator(
    task_id='extract_details',
    python_callable=extract_details,
    provide_context=True,
    dag=dag,
)

fetch_weather_data_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data_task,
    provide_context=True,
    dag=dag,
)

merge_and_save_task = PythonOperator(
    task_id='merge_and_save_results',
    python_callable=merge_and_save_results,
    provide_context=True,
    dag=dag,
)

# Task dependencies
load_csv_task >> extract_details_task >> fetch_weather_data_task >> merge_and_save_task
