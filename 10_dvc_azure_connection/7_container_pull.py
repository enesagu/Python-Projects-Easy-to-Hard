from azure.storage.blob import BlobServiceClient
import os

def download_container(connection_string, container_name, local_folder):
    # Connection to Blob Service
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get Container Client
    container_client = blob_service_client.get_container_client(container_name)

    # List blobs in the container
    blob_list = container_client.list_blobs()

    # Create local folder if it doesn't exist
    os.makedirs(local_folder, exist_ok=True)

    # Download each blob
    for blob in blob_list:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
        download_file_path = os.path.join(local_folder, blob.name)
        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

def main():
    # Azure account info
    connection_string = "string"

    # Container name
    container_name = "name"

    # Local folder to save the downloaded files
    local_folder = "path"

    # Download container
    download_container(connection_string, container_name, local_folder)

    print("Container downloaded successfully.")

if __name__ == "__main__":
    main()
