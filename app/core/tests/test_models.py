"""
Test user model
"""
from datetime import datetime
from django.test import TestCase
from core import models
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test Model"""

    # def test_create_user_with_email(self):
    #     """Creating user with email"""
    #     email = "test_user@example.com"
    #     password = 'test_pass'
    #     user = get_user_model().objects.create_user(email=email,
    #                                            password=password)
        
    #     self.assertEqual(user.email, email)
    #     self.assertTrue(user.check_password(password))

    # def test_new_user_email_normalise(self):
    #     """Test for email"""
    #     sample_emails = [
    #         ["test1@EXAMPLE.com","test1@example.com"],
    #         ["Test2@Example.com","Test2@example.com"],
    #         ["TEST3@EXAMPLE.COM","TEST3@example.com"],
    #         ["test4@example.COM","test4@example.com"]
    #     ]

    #     for email, expected in sample_emails:
    #         user = get_user_model().objects.create_user(email, 'sample123')
    #         self.assertEqual(user.email, expected)

    # def test_new_user_without_email(self):
    #     """Test for user without email"""
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user("","test123")

    # def test_create_superuser(self):
    #     """Test creating a superuser"""
    #     user = get_user_model().objects.create_superuser("test@example.com",
    #                                                      "test123")
        
    #     self.assertTrue(user.is_superuser)
    #     self.assertTrue(user.is_staff)
        
    def test_create_projects(self):
        """Test creating a project is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        project = models.Projects.objects.create(
            user=user,
            title='Sample project name',
            start_date='2012-12-12',
            end_date='2021-12-12',
            description='Sample project description.',
        )

        self.assertEqual(str(project), project.title)