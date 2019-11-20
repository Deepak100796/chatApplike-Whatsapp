import uuid

from django.shortcuts import render

from .models import Message

from django.http import JsonResponse
# Create your views here.

def index(request):
    uid4 = str(uuid.uuid4())
    return render(request, 'chat/index.html', {'uid4': uid4})


def room(request, room_name):
    try:
        chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
        return render(request, 'chat/room.html', {
            'chat_messages': chat_messages,
            'room_name': room_name
        })
    except Exception as e:
        print(e,">>>>>>>>>>>>>>>>")
        return JsonResponse({"exp":"hgfhfh"})