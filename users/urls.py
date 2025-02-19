from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, register_view, CustomPasswordResetView, edit_profile, user_profile
from django.contrib import messages
 # 🚀 Enhancement: Namespacing for better URL management

urlpatterns = [
    path("login/", login_view, name="login"),
    
    # 🚀 Enhancement: Logout with a message
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("register/", register_view, name="register"),
    
    # 🚀 Enhancement: Use slug instead of username for profile URL
    path('<slug:username>/', user_profile, name='user_profile'),
    
    path("reset-password/", CustomPasswordResetView.as_view(), name="reset_password"),
    
    path('edit/', edit_profile, name='edit_profile'),
    path('users/edit/', edit_profile, name='edit_profile'),  # 🛠️ Add this

]
