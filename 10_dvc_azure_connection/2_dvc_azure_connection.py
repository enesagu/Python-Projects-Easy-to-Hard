import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import dvc.api

# Set up Azure Blob Storage credentials
AZURE_STORAGE_CONNECTION_STRING = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
CONTAINER_NAME = "your_container_name"
BLOB_NAME = "your_blob_name"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

# Download dataset from Azure Blob Storage
with dvc.api.open_url(f"azure://{CONTAINER_NAME}/{BLOB_NAME}", mode="r", remote="azure") as f:
    df = pd.read_csv(f)

# Preprocess data (example: splitting into features and target)
X = df.drop(columns=["target_column"])
y = df["target_column"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train machine learning model (example: Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

# Save trained model to Azure Blob Storage
MODEL_BLOB_NAME = "your_model.pkl"
with dvc.api.open_url(f"azure://{CONTAINER_NAME}/{MODEL_BLOB_NAME}", mode="w", remote="azure") as f:
    pickle.dump(model, f)

# Log evaluation metrics
with dvc.api.open_url(f"azure://{CONTAINER_NAME}/metrics.json", mode="a", remote="azure") as f:
    json.dump({"train_score": train_score, "test_score": test_score}, f)
