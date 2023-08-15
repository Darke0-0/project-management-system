"""
Create your models here.
"""

from typing import Any
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """User Manager"""
    
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have a email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create, save and return a superuser"""
        user = self.create_user(email=email,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Projects(models.Model):
    """Project Model"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    team_lead = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    costing = models.DecimalField(max_digits=8,decimal_places=2)
    tags = models.ManyToManyField('Tag',blank=True)
    components = models.ManyToManyField('Components',blank=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    """Tag for filtering projects."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name


class Components(models.Model):
    """Components for projects."""
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model())
    client = models.CharField(max_length=255,null=True)
    priority = models.CharField(max_length=255,default='None')
    file = models.FileField(null=True)

    def __str__(self):
        return self.name

class Chat(models.Model):
    """Chat Model"""
    room_name = models.CharField(max_length=20,blank=True)
    users = models.ManyToManyField(get_user_model())
    message = models.ManyToManyField('Messages',blank=True)

    def __str__(self):
        return self.room_name

class Messages(models.Model):
    """Messages Model"""
    sender = models.ManyToManyField(get_user_model(),blank=True)
    room = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class GroupChat(models.Model):
    """Group Chat Model"""
    project = models.OneToOneField(Projects, on_delete=models.CASCADE)
    users = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.project

class GroupMessage(models.Model):
    """Group Messages Model"""
    room = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
