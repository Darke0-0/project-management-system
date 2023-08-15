"""
Views for the projects APIs
"""
from rest_framework import viewsets
from rest_framework import generics

from django.contrib.auth import get_user_model
from core.models import Projects, Tag, Components
from projects import serializers
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from django.contrib.auth.mixins import LoginRequiredMixin

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
        if serializer.is_valid():
            serializer.save()
            project_link = serializer
            return render(request, 'project-details.html', context={'project_link':project_link})
        else:
            # message = serializer.error_messages
            return render(request, 'new-project.html', {'serializer': serializer})

class ProjectDetailsView(generics.CreateAPIView, LoginRequiredMixin):
    serializer_class = serializers.ProjectsSerializer
    queryset = Projects.objects.all()

    # def get_queryset(self):
    #     """Retrieve projects for authenticated user."""
    #     return self.queryset.filter(user=self.request.user,project=self.request.project).order_by('-id')
    
    def get(self, request):
        queryset = self.get_queryset()
        return render(request, "project-details.html", {'queryset': queryset})

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
        serialized_data = self.serializer_class(self.queryset, many=True).data
        return self.queryset
    
    def get(self, request):
        queryset = self.get_queryset()
        return render(request, "user-project.html", {'queryset': queryset})

class BaseProjectAttrViewSet(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """Base viewset for recipe attributes."""
    

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(recipe__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()
    
class TagViewSet(BaseProjectAttrViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()


class IngredientViewSet(BaseProjectAttrViewSet):
    """Manage ingredients in the database."""
    serializer_class = serializers.ComponentsSerializer
    queryset = Components.objects.all()

# Helper Function
def load_users(request):
    users = get_user_model().objects.values('id', 'name')
    return JsonResponse(list(users), safe=False)
