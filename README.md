# 🧠 AI Assistant (Django + LM Studio)

A simple **AI Assistant Web App** built with **Django** that connects to a **local AI model** via **LM Studio**.  
The assistant works like a mini ChatGPT — users can type queries, get responses, and see conversation history (only for the current session, no database storage).  

---

## 🚀 Features
- Local AI inference (no paid APIs required).  
- Uses **Llama-3.2-3B-Instruct-Q8_0.GGUF** (or any GGUF model supported by LM Studio).  
- Web-based interface (similar to ChatGPT).  
- Keeps chat history only during the session.  
- Lightweight and beginner-friendly project.  

---

## 🛠️ Requirements
- Python 3.9+  
- Django 4+  
- LM Studio (for running local models)  
- Installed Python libraries:
````bash
  pip install django requests
````

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-assistant-django.git
cd ai-assistant-django
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

*(Make sure `requirements.txt` contains at least: `django`, `requests`)*

### 3️⃣ Setup LM Studio

1. Download and install [LM Studio](https://lmstudio.ai/).
2. In **LM Studio → Models tab**, download your model (e.g., **Llama-3.2-3B-Instruct-Q8\_0.GGUF**).
3. Open **Server tab** in LM Studio.
4. Start the local API (default: `http://localhost:1234`).

---

## ▶️ Running the Project

### Start Django Server

```bash
python manage.py runserver
```

### Access the Web App

Open in your browser:
👉 `http://127.0.0.1:8000/`

---

## 💻 Usage

1. Type your question in the input box.
2. Click **Send**.
3. The AI response will appear above, like a chat.
4. Conversation history stays visible until you refresh or close the session.

---

## 📂 Project Structure

```
ai_assistant/        # Main Django project folder
├── ai_assistant/    # Project settings
├── chatbot/         # App folder
│   ├── templates/   # HTML template (chat.html)
│   ├── views.py     # Chat logic
│   ├── ai_model.py  # LM Studio API connector
│   └── urls.py
└── manage.py
```

---

## 🧩 How It Works

* **Frontend**: Simple chat interface (`chat.html`).
* **Backend**: Django view handles requests.
* **AI Model**: LM Studio runs locally and exposes an OpenAI-style API (`/v1/chat/completions`).
* **Connector**: `ai_model.py` sends user input → LM Studio → gets response → displays on UI.

---

## 🔮 Future Improvements

* Add user accounts + persistent chat history.
* Support multiple models (switch from UI).
* Add streaming responses (typing effect).
* Mobile-friendly UI with TailwindCSS.

---

## 🙌 Credits

* [Django](https://www.djangoproject.com/) for the web framework.
* [LM Studio](https://lmstudio.ai/) for running local LLMs.
* [Meta AI](https://ai.meta.com/) for Llama models.

---


