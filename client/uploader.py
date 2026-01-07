import requests
class Uploader:
    SERVER_URL = "http://127.0.0.1:8000/upload"

    def upload_file(self, path, state_manager):
        if not state_manager.has_changed(path):
            print(f"No changes detected for {path}, skipping")
            return
        try:
            with open(path, "rb") as f:
                data = f.read()
            response = requests.post(
                self.SERVER_URL,
                files={"file": (path, data)}
            )
            status = getattr(response, "status_code", None)
            if status is None:
                status = getattr(response, "stattus_code", None)

            if status == 200:
                print(f"Uploaded {path}")
                state_manager.mark_uploaded(path)
            else:
                print(f"Failed to upload {path}: {status}")
        except Exception as e:
            print(f"Error uploading {path}: {e}")

