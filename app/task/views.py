from rest_framework import viewsets
from rest_framework import generics

from django.contrib.auth import get_user_model
from core.models import Task, Projects
from task import serializers
import projects
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from django.shortcuts import render

from django.core.serializers import serialize
import json

class TaskViewSet(viewsets.ModelViewSet):
    """View for manage task APIs."""
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self,user):
        """Retrieve task for authenticated user."""
        print('query_set',user)
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.TaskSerializer

        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new task."""
        serializer.save(user=self.request.user)


class TaskDetailsView(generics.CreateAPIView, LoginRequiredMixin):
    serializer_class = projects.serializers.ProjectsSerializer
    print(serializer_class)
    queryset = Projects.objects.all()
    taskset = Task.objects.all()
    
    def get(self, request, project_id):
        self.queryset = self.queryset.filter(id=project_id)

        self.taskset = self.taskset.filter(project=project_id)
        self.taskset = serialize("json", self.taskset)
        self.taskset = json.dumps(self.taskset)

        return render(request, "board.html", {'queryset': self.queryset,'taskset':self.taskset})
    
    def post(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        data = dict(request.data)
        print(data)
        if serializer.is_valid():
            # serializer.save()
            print(data)
            task_link = serializer
            return render(request, 'board.html', context={'task_link':task_link})
        else:
            # message = serializer.error_messages
            return render(request, 'board.html', {'serializer': serializer})
        
class TaskCreateView(generics.CreateAPIView, LoginRequiredMixin):
    serializer_class = serializers.TaskSerializer
    