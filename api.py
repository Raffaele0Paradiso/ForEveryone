import requests
import json

url = "https://api.dify.ai/v1/completion-messages"

headers = {
'Authorization': 'Bearer ENTER-YOUR-SECRET-KEY',
'Content-Type': 'application/json',
}

data = {
"inputs": {"text": 'Hello, how are you?'},
"response_mode": "streaming",
"user": "abc-123"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)