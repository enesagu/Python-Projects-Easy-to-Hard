from azure.storage.blob import BlobServiceClient
import os

def download_blob(storage_connection_string, container_name, local_folder):
    # Create Blob service client
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

    # Get container client
    container_client = blob_service_client.get_container_client(container_name)

    # List blobs in the container
    blob_list = container_client.list_blobs()

    # Ensure local folder exists
    os.makedirs(local_folder, exist_ok=True)

    # Download each blob
    for blob in blob_list:
        # Construct blob name and destination file path
        blob_name = blob.name
        download_file_path = os.path.join(local_folder, blob_name)

        # Download the blob
        with open(download_file_path, "wb") as download_file:
            download_file.write(container_client.download_blob(blob_name).readall())

    print("All blobs have been successfully downloaded.")

if __name__ == "__main__":
    # Azure Blob storage connection string
    storage_connection_string = "string"
    
    # Name of the Blob container to download from
    container_name = "name"
    
    # Local folder where downloaded files will be saved
    local_folder = "test"

    # Download blobs
    download_blob(storage_connection_string, container_name, local_folder)
