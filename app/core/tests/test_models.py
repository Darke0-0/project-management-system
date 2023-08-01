"""
Test user model
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test Model"""

    def test_create_user_with_email(self):
        """Creating user with email"""
        email = "test_user@example.com"
        password = 'test_pass'
        user = get_user_model().objects.create(email=email,
                                               password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))