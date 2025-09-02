import requests
import base64
import json

# -----------------------
# CONFIG
# -----------------------
FUNCTION_URL = "http://localhost:7071/api/ExtractTextFromDocument"
FILE_PATH = "tests/files/example.pdf"  # relative to the repo root"  # or "example.pdf"

# -----------------------
# Read and encode file
# -----------------------
with open(FILE_PATH, "rb") as f:
    file_bytes = f.read()
    encoded_content = base64.b64encode(file_bytes).decode("utf-8")

# -----------------------
# Prepare JSON payload
# -----------------------
payload = {
    "filename": FILE_PATH.split("/")[-1],  # just the file name
    "filecontent": encoded_content
}

# -----------------------
# Send POST request
# -----------------------
response = requests.post(
    FUNCTION_URL,
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

# -----------------------
# Print results
# -----------------------
if response.status_code == 200:
    print("✅ Extracted text:\n")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}: {response.text}")
