import io
from minio import Minio
import hashlib
import json
from datetime import datetime
from typing import BinaryIO

class MinIOStorage:
    #ctor
    def __init__(
        self,
        endpoint: str,
        access_key: str,
        secret_key: str,
        bucket_name: str,
        secure: bool = False,
        metadata_file: str = "metadata.json"
    ):
        self.client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )
        self.bucket = bucket_name
        #self.metadata_file = metadata_file

        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)

        try:
            with open(self.metadata_file, "r") as f:
                self.metadata = json.load(f)
        except FileNotFoundError:
            self.metadata = {}
    
    #hashing function
    def _hash_file(self, data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()
    #save function
    def save(self, filename: str, file: BinaryIO) -> dict:
        data = file.read()
        file_hash = self._hash_file(data)

        if file_hash in self.metadata:
            return {
                "status": "duplicate",
                "message": "File already exists",
                "hash": file_hash
            }

        self.client.put_object(
            bucket_name=self.bucket,
            object_name=filename,
            data=io.BytesIO(data),
            length=len(data)
        )

        meta = {
            "filename": filename,
            "hash": file_hash,
            "size": len(data),
            "uploaded_at": datetime.utcnow().isoformat()
        }

        self.metadata[file_hash] = meta
        self._save_metadata()

        return meta
    #save metadata function
    def _save_metadata(self):
        with open(self.metadata_file, "w") as f:
            json.dump(self.metadata, f, indent=2)
