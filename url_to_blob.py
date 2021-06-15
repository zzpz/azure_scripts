from azure.storage.blob import BlobClient, PublicAccess
import os


def direct_import():
    """
    script to directl import a file from a url to an azure blob.
    fails if the source url is aws s3.
    requires s3 keys to do so, even if file is public.

    """

    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = "container_name"
    blob_name = "blob_name"

    blob_client = BlobClient.from_connection_string(conn_str, container_name, blob_name)

    source_url = "https://images.unsplash.com/photo-1622228389110-88e593d17a3f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80"
    # source_url = "https://nyc-tlc.s3.amazonaws.com/trip+data/fhvhv_tripdata_2020-10.csv"

    blob_client.start_copy_from_url(source_url, metadata=None, incremental_copy=False)


# Main method.
if __name__ == "__main__":
    direct_import()
