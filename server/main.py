from fastapi import FastAPI, UploadFile, File
from storage import MinIOStorage

app = FastAPI()
storage = MinIOStorage(
    endpoint="localhost:9000",
    access_key="NoaK",
    secret_key="@4110803",
    bucket_name="assets",
    secure=False
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    data = await file.read()
    storage.upload(file.filename, data)
    return {"status": "ok", "filename": file.filename}
