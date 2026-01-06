from minio import Minio
import io

class MinIOStorage:
    def __init__(self,endpoint: str, access_key: str, secret_key: str,bucket_name: str,secure: bool = False):
        self.bucket = bucket_name
        self.client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )
        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)


    def upload(self, filename: str, data: bytes):
        self.client.put_object(
            bucket_name=self.bucket,
            object_name=filename,
            data=io.BytesIO(data),
            length=len(data)
        )
