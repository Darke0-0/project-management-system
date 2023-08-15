from django.shortcuts import render, redirect
from core.models import Chat, Messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from chat import serializers
from django.http import JsonResponse

class ChatRoomView(generics.CreateAPIView, LoginRequiredMixin):
    serializer_class = serializers.ChatSerializer
    
    def create_room(request):
        if request.method == 'POST':
            # Create a new chat room
            name = request.POST.get('name')
            room = Chat.objects.create(name=name)

            return redirect('chat_room', room_id=room.id)

        return render(request, 'message.html')
        
    def get(self, request):
        return render(request, "message.html")
    
# Helper
def chat_room(request,user_id):
    # Retrieve the chat room and related messages
    # room = Chat.objects.values()
    room = Chat.objects.filter(users=request.user.id)
    room = room.filter(users=user_id).first()
    messages = Messages.objects.all()
    messages = messages.filter(room=room)
    return JsonResponse(list(messages),safe=False)