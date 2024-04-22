import requests
import subprocess

# Function to ping a website and get the round-trip time
def ping_website(website):
    try:
        # Ping the website and capture the output
        ping_result = subprocess.run(["ping", "-c", "4", website], capture_output=True, text=True)
        
        # Extract the round-trip time from the ping output
        time_lines = [line for line in ping_result.stdout.split("\n") if "time=" in line]
        rt_times = [float(line.split("time=")[1].split()[0]) for line in time_lines]
        
        # Calculate average round-trip time
        avg_rt_time = sum(rt_times) / len(rt_times)
        
        print(f"Ping statistics for {website}:")
        print(f"Avg round-trip time: {avg_rt_time} ms")
        
    except Exception as e:
        print(f"Error: {e}")

# Function to fetch HTTP headers of a website
def get_http_headers(website):
    try:
        # Send a HEAD request to the website to get headers
        response = requests.head(website)
        
        print(f"HTTP Headers for {website}:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
            
    except Exception as e:
        print(f"Error: {e}")

# Function to fetch content from a website
def fetch_website_content(website):
    try:
        # Send a GET request to the website to fetch content
        response = requests.get(website)
        
        print(f"Content from {website}:")
        print(response.text)
            
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    website = "https://www.example.com"
    
    # Ping the website
    print("\n")
    print("-" * 20 + " Pinging Website " + "-" * 20)
    ping_website(website)
    
    # Get HTTP headers
    print("\n")
    print("-" * 20 + " HTTP Headers " + "-" * 20)
    get_http_headers(website)
    
    # Fetch website content
    print("\n")
    print("-" * 20 + " Website Content " + "-" * 20)
    fetch_website_content(website)

if __name__ == "__main__":
    main()
