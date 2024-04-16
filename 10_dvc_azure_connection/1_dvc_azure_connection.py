import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Step 1: Set up Azure credentials
# This code assumes that you have already set up your Azure account and have access to the storage account.
# We'll use DefaultAzureCredential to authenticate with Azure. This credential automatically uses environment variables,
# managed identity, or Azure CLI authentication depending on the environment.
credential = DefaultAzureCredential()

# Step 2: Define your Azure Storage account name and container name
storage_account_name = "your_storage_account_name"
container_name = "your_container_name"

# Step 3: Set up a BlobServiceClient using the Azure credentials
# BlobServiceClient is used to interact with the Blob storage accounts.
blob_service_client = BlobServiceClient(
    account_url=f"https://{storage_account_name}.blob.core.windows.net",
    credential=credential
)

# Step 4: Create a container if it doesn't exist
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
except Exception as e:
    print(f"An error occurred while creating the container: {e}")

# Step 5: Upload files to Azure Blob Storage
# Assuming you have a directory with files to upload
local_directory = "/path/to/your/local/directory"
for root, dirs, files in os.walk(local_directory):
    for file in files:
        local_file_path = os.path.join(root, file)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)

# Step 6: List the files in the container to verify the upload
print("Files in the container:")
blob_list = container_client.list_blobs()
for blob in blob_list:
    print(f"- {blob.name}")
