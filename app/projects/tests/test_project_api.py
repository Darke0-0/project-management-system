"""
Test for Project API 
"""
"""
Tests for project APIs.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Projects

from projects.serializers import ProjectsSerializer


PROJECT_URL = reverse('project:project-list')


def create_project(user, **params):
    """Create and return a sample project."""
    defaults = {
        'title': 'Sample project title',
        'start_data': '2012-12-12',
        'end_date': '2021-12-12',
        'description': 'Sample description',
    }

    defaults.update(params)

    project = Projects.objects.create(user=user, **defaults)
    return project


class PublicProjectsAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    # def test_auth_required(self):
    #     """Test auth is required to call API."""
    #     res = self.client.get(PROJECT_URL)

    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProjectsApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    # def test_retrieve_projects(self):
    #     """Test retrieving a list of projects."""
    #     create_project(user=self.user)
    #     create_project(user=self.user)

    #     res = self.client.get(PROJECT_URL)

    #     projects = Projects.objects.all().order_by('-id')
    #     serializer = ProjectsSerializer(projects, many=True)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(res.data, serializer.data)

    # def test_project_list_limited_to_user(self):
    #     """Test list of projects is limited to authenticated user."""
    #     other_user = get_user_model().objects.create_user(
    #         'other@example.com',
    #         'password123',
    #     )
    #     create_project(user=other_user)
    #     create_project(user=self.user)

    #     res = self.client.get(PROJECT_URL)

    #     projects = Projects.objects.filter(user=self.user)
    #     serializer = ProjectsSerializer(projects, many=True)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(res.data, serializer.data)