from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Azure account info
connection_string = "string"

# Connection blob service
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# container and file name
container_name = "container_name"
file_name = "example1.txt"

# Download file from blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
downloaded_blob = blob_client.download_blob()

# read file
file_content = downloaded_blob.readall()


#  print terminal
print("Downloaded file content:")

print(file_content.decode('utf-8'))


with open("/home/user/Desktop/example123.txt","wb") as file:
    file.write(file_content)