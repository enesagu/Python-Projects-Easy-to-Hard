import boto3

def main():
    """
    Connect to AWS S3 and retrieve a list of buckets.

    This function demonstrates how to establish a connection with AWS S3 using the Boto3 library
    in Python. It retrieves a list of all buckets in the specified region and prints their names.

    AWS Access Keys and Region:
    - Replace 'YOUR_ACCESS_KEY_ID' and 'YOUR_SECRET_ACCESS_KEY' with your own AWS access key ID and secret access key.
    - Replace 'YOUR_REGION' with the AWS region you want to connect to.

    Returns:
    None
    """
    # Set AWS credentials and region
    aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
    aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
    region_name = 'YOUR_REGION'

    # Create a Boto3 S3 client
    s3 = boto3.client('s3', 
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region_name)

    try:
        # Retrieve the list of S3 buckets
        response = s3.list_buckets()

        # Print the list of buckets
        print("S3 Bucket List:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
