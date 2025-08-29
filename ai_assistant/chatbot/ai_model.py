import requests

API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "local-model"  # LM Studio uses this alias by default

def get_ai_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"
