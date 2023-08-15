from django.urls import path, include
from chat import views
from rest_framework.routers import DefaultRouter
 
# router = DefaultRouter()
# # router.register('chat', views.ProjectsViewSet)

app_name = 'chat'

urlpatterns = [
    path("chatroom/", views.ChatRoomView.as_view(), name="chatroom"),
    path('joinroom/<int:user_id>', views.chat_room, name="room")
]