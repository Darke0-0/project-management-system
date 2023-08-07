"""
Views for the projects APIs
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import View
from .forms import ProjectCreateForm

from django.contrib.auth import get_user_model
from core.models import Projects
from projects import serializers

from django.http import JsonResponse
from django.shortcuts import render

class ProjectsViewSet(viewsets.ModelViewSet):
    """View for manage projects APIs."""
    serializer_class = serializers.ProjectsDetailSerializer
    queryset = Projects.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve projects for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ProjectsSerializer

        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new project."""
        serializer.save(user=self.request.user)

class ProjectCreateView(View):
    
    def get(self, request):
        return render(request, template_name="new-project.html")
    
    def post(self, request):
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            form.save() 
            # return redirect('mymodel_list')
        else:
            form = ProjectCreateForm()

# Helper Function
def load_users(request):
    users = get_user_model().objects.values('id', 'name')
    print(users)
    return JsonResponse(list(users), safe=False)