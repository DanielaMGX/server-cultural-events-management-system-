import asyncio
from google.cloud import storage
from google.oauth2 import service_account

class ServiceBackend:
    key_path = "app/key/service-account-file.json"
    credentials = service_account.Credentials.from_service_account_file(key_path)
    storage_client = storage.Client(credentials=credentials)

    @staticmethod
    async def upload_blob_async(bucket_name, destination_blob_name, contents):
        try:
            bucket = ServiceBackend.storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, blob.upload_from_string, contents)
            return True
        except Exception as e:
            print(e)
            return False

service_backend = ServiceBackend