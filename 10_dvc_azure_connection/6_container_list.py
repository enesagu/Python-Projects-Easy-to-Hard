from azure.storage.blob import BlobServiceClient

# Azure account 
connection_string = "string"

# Blob  connection
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# list all container
containers = blob_service_client.list_containers()

# write all list
print("Container list:")
for container in containers:
    print(container.name)
