# Asset Catalog Project

## 📁 File Sync Service

An intelligent system for automatic file synchronization that monitors a local folder and uploads changes to a server in real-time.

---

## 🏗️ Project Structure

- **client/**: The client monitors the folder and sends files to the server.  
- **server/**: The target server that receives and stores files.  
- **tests/**: Automated tests for various units of the project.  

---

## ⚙️ Installation

Install the required libraries (recommended inside a virtual environment):

🔹 `pip install -r client/requirements.txt`

---

## 🚀 Running the Project

### 1️⃣ Start the Server
The server temporarily listens at `http://127.0.0.1:8000/upload`:

🔹 `python -m uvicorn main:app --reload`



### 2️⃣ Start the Client (Monitor)
The client performs an initial scan of the folder and then starts listening for changes:

🔹 `python client/cli.py run "C:\path\to\your\folder"`

---

## 🧪 Running Tests

The project uses `pytest` for testing.  

To run all tests:

🔹 `python -m pytest -q`

---

## 🛠️ Key Features

- **Initial Scan**: Scans the folder on every start and uploads files that changed while the system was offline.  
- **Hash Validation**: Uses SHA-256 to ensure only truly changed files are uploaded.  
- **Clean Repo**: Built-in `.gitignore` to prevent uploading junk files like `__pycache__`.  

---
