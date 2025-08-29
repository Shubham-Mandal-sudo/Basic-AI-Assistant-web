from django.shortcuts import render , redirect
from .ai_model import get_ai_response

def chat_view(request):
    conversation = request.session.get("conversation", [])

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            ai_reply = get_ai_response(user_input)

            conversation.append(("You", user_input))
            conversation.append(("AI", ai_reply))
            request.session["conversation"] = conversation
        return redirect('chat')

    return render(request, "chatbot\chat_e.html", {"conversation": conversation})
