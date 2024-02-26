# main/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm  
from django.contrib.auth.decorators import login_required

def some_view_function(request):
    return render(request, 'main/base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'main/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a related UserProfile
            user_profile = UserProfile.objects.create(user=user)  # Modify this according to your UserProfile model

            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'main/register.html', {'form': form})


def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'user_profile': user_profile})

@login_required
def home(request):
    return render(request, 'main/home.html', {'welcome_message': 'Welcome to the life of the party!'})
