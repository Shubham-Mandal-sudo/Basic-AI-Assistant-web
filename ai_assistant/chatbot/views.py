from django.shortcuts import render , redirect
from .ai_model import get_ai_response
from django.utils import timezone

def chat_view(request):
    if "new_chat" in request.POST:
        # Clear conversation history
        request.session["conversation"] = []
    conversation = request.session.get("conversation", [])

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            ai_reply = get_ai_response(user_input)
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

            conversation.append({
                "sender": "You",
                "message": user_input,
                "timestamp": timestamp
            })
            conversation.append({
                "sender": "AI",
                "message": ai_reply,
                "timestamp": timestamp
            })

            request.session["conversation"] = conversation
        return redirect('chat')

    return render(request, "chatbot/chat.html", {"conversation": conversation})

