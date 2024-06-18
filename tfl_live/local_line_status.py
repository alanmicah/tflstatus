import json, os, requests
from dotenv import load_dotenv
load_dotenv()

url = "http://localhost:5050/webhook"

token = os.environ.get('LOCAL_WEBHOOK_TOKEN')

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {token}"
}

# Data to be sent to the webhook
data = {
    "message": "Hello from another script!",
    "timestamp": "2024-06-14T12:34:56Z"
}

# Convert data to JSON
json_data = json.dumps(data)

# Send POST request
response = requests.post(url, headers=headers, data=json_data)

# Print the response from the server
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")