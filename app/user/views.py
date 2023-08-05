"""
Views for the user API.
"""
from django import forms
from django.contrib.auth import login, authenticate

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from django.views.generic import View
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.views import AuthenticationForm

from rest_framework import status
from django.shortcuts import redirect, render
from user.serializers import (
    UserSerializer,
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

    def get(self, request):
        # Create a new instance of the serializer to render the form
        serializer = self.get_serializer()
        return render(request, 'new-account.html', {'serializer': serializer})
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginPageView(View):
    
    def get(self, request):
        return render(request, template_name="user-login.html")
        
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                print('login')
                login(request, user)
                return redirect('user-profile.html')
        message = 'Login failed!'
        return render(request, 'user-login.html', context={'login-form': form, 'message': message})

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class
        return render(request, 'new-account.html', {'serializer': serializer})
    
