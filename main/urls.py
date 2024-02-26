# main/urls.py
from django.urls import path
from .views import some_view_function, user_login, user_logout, register_user, view_profile, home  

urlpatterns = [
    path('', some_view_function, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', view_profile, name='view_profile'), 
    path('home/', home, name='home'), 
]