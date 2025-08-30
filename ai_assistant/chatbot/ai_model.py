from markdown_it import MarkdownIt
import requests

API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "local-model"

md = MarkdownIt()

def get_ai_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 300
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        text = response.json()["choices"][0]["message"]["content"]
        html = md.render(text)  # Convert Markdown → HTML
        return html
    else:
        return f"<p><strong>Error:</strong> {response.text}</p>"
