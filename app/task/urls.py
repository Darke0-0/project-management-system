"""
URL mappings for the project app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from task import views

router = DefaultRouter()
router.register('task', views.TaskViewSet)

app_name = 'task'

urlpatterns = [
    path('', include(router.urls)),
    path('view_task/<int:project_id>', views.TaskDetailsView.as_view(), name='view_task'),
]