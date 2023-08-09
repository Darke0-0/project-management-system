"""
URL mappings for the project app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register('projects', views.ProjectsViewSet)

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
    path('createproject/', views.ProjectCreateView.as_view(), name='create_project'),
    path('userproject/', views.ProjectSetView.as_view(), name='user_project'),
    path('load_users/', views.load_users, name='load_users'),
]