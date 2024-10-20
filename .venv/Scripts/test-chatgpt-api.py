import sys
import requests
import json

api_key = sys.argv[1]
api_url = 'https://api.openai.com/v1/chat/completions'

# Set up the headers with the API key
headers = {
    'Authorization': 'Bearer '+api_key,
    'Content-Type': 'application/json'
}

# Define the messages for the conversation
data = {
    "model": "gpt-3.5-turbo",  # Specify model (gpt-3.5-turbo or gpt-4)
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How can I use the ChatGPT REST API from Python?"}
    ],
    "temperature": 0.7
}

# Make the request to the API
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Check for a successful response
if response.status_code == 200:
    # Parse the response content
    result = response.json()
    # Extract and print the assistant's reply
    print(result['choices'][0]['message']['content'])
else:
    print("Error: "+str(response.status_code))
    print(response.text)
