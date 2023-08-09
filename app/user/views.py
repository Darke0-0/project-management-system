"""
Views for the user API.
"""
from django.contrib.auth import login, authenticate

from rest_framework import generics
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm


from django.shortcuts import redirect, render
from user.serializers import (
    UserSerializer,
)

from django.contrib.auth.mixins import LoginRequiredMixin


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

    def get(self, request):
        # Create a new instance of the serializer to render the form
        serializer = self.get_serializer()
        return render(request, 'new-account.html', {'serializer': serializer})
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            message = 'Registration Successful'
            return render(request, 'user-login.html', context={'message': message})
        message = serializer.error_messages
        return render(request, 'new-account.html', {'serializer': serializer, 'message':message})

class LoginPageView(View):

    def get(self, request):
        return render(request, "user-login.html")
        
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('../me',request=request,permanent=True)
            # return render(request, 'user-profile.html', context={'login-form': form, 'message': message})
        message = 'Login failed!'
        return render(request, 'user-login.html', context={'login-form': form, 'message': message})

class ManageUserView(generics.RetrieveUpdateAPIView, LoginRequiredMixin):
    """Manage the authenticated user."""
    serializer_class = UserSerializer

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class
        return render(request, 'new-account.html', {'serializer': serializer})

# Logout
def logout(request):
    try:
        del request.session['_auth_user_id']
        return redirect('user')
    except:
        return render(request, 'user-project.html')