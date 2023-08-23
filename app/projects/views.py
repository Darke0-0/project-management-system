"""
Views for the projects APIs
"""
from rest_framework import viewsets
from rest_framework import generics

from django.contrib.auth import get_user_model
from core.models import Projects, Task
from projects import serializers
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
import json

from django.http import JsonResponse
from django.shortcuts import render

class ProjectsViewSet(viewsets.ModelViewSet):
    """View for manage projects APIs."""
    serializer_class = serializers.ProjectsDetailSerializer
    queryset = Projects.objects.all()
    

    def get_queryset(self,user):
        """Retrieve projects for authenticated user."""
        print('query_set',user)
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ProjectsSerializer

        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new project."""
        serializer.save(user=self.request.user)

class ProjectCreateView(generics.CreateAPIView, LoginRequiredMixin):
    serializer_class = serializers.ProjectsSerializer
    
    def get(self, request):
        serializer = self.get_serializer()
        return render(request, "new-project.html", {'serializer': serializer} )
    
    def post(self, request):
        serializer = serializers.ProjectsSerializer(data=request.data)
        data = dict(request.data)
        # Formatting data
        data.pop("csrfmiddlewaretoken")
        data['title'] = data['title'][0]
        data['team_lead'] = get_user_model().objects.get(id=data['team_lead'][0])
        data['start_date'] = data['start_date'][0]
        data['end_date'] = data['end_date'][0]
        data['client'] = data['client'][0]
        data['priority'] = data['priority'][0]
        data['description'] = data['description'][0]
        data['costing'] = float(data['costing'][0])
        users = None
        if serializer.is_valid():

            users = get_user_model().objects.filter(id=users)
            instance = serializer.create(data)

            instance.users.set(users)

            project_link = serializer
            return render(request, 'project-details.html', context={'project_link':project_link})
        else:
            # message = serializer.error_messages
            return render(request, 'new-project.html', {'serializer': serializer})

class ProjectCalenderView(generics.CreateAPIView, LoginRequiredMixin):
    serializers = serializers.ProjectsSerializer
    queryset = Projects.objects.all()

    def project_set(self):
        self.queryset = Projects.objects.values('title','start_date','end_date')
        self.queryset = self.queryset.filter(team_lead=self.user)
        return JsonResponse(list(self.queryset),safe=False)

    def get(self, request):
        return render(request, "calendar.html")

class ProjectSetView(generics.CreateAPIView, LoginRequiredMixin):
    serializer_class = serializers.ProjectsSerializer
    queryset = Projects.objects.all()

    def get_queryset(self):
        """Retrieve projects for authenticated user."""
        user = self.request.user
        self.queryset = self.queryset.filter(team_lead=user)
        return self.queryset
    
    def get(self, request):
        queryset = self.get_queryset()
        return render(request, "user-project.html", {'queryset': queryset})

# Helper Function
def load_users(request):
    users = get_user_model().objects.values('id', 'name')
    return JsonResponse(list(users), safe=False)
