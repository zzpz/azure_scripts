from azure.storage.blob import BlobServiceClient, PublicAccess
import os


def upload():
    """
    Script to upload multiple simliarly named csv files with incrementing suffixes to azure blob storage. Creates container if not exists. Fails is container exists.

    Args:
        None

    Returns:
        None

    Raises:
    """
    # conn str
    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)

    # name container
    container_name = "container_name"

    # create container (will fail if already exists)
    container_client = blob_service_client.create_container(container_name)

    # upload from local directory
    local_path = "./folder_of_csvfiles"

    # loop files for upload
    fn = "filename"
    mo = ["{:02}".format(num) for num in range(1, 13)]

    for m in mo:
        local_file_name = f"{fn}-{m}.csv"
        upload_file_path = os.path.join(local_path, local_file_name)

        blob_client = blob_service_client.get_blob_client(
            container=container_name, blob=local_file_name
        )

        print(f"uploading file: {local_file_name}")
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)


# Main method.
if __name__ == "__main__":
    upload()
