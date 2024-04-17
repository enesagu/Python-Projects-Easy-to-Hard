from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Azure account info
connection_string = "string"

# Connection Blob service
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Container name
container_name = "container_name"

# Text file
file_content = "This text loaded blob"
file_name = "example1.txt"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
blob_client.upload_blob(file_content)

print("Text uploaded")
