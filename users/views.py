from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from blogs.models import Blog
from .forms import UserProfileForm, UserUpdateForm, CustomPasswordChangeForm
from .models import UserProfile


# 🚀 Enhanced Login View: Better UX & Redirect Handling
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            return render(request, "login.html", {"error": "⚠️ No wizard found with this name!"})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", "home")  # Redirects back to the last visited page
            return redirect(next_url)
        else:
            return render(request, "login.html", {"error": "❌ Incorrect Secret Spell!"})

    return render(request, "login.html")


# 🚀 Enhanced Registration View: Prevent Duplicate Wizards
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "🛑 Wizard name already taken!"})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "📜 A wizard with this scroll address already exists!"})

        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, slug=username)  # 🚀 Auto-create profile
        login(request, user)
        return redirect("home")

    return render(request, "register.html")


# 🔑 Password Reset View (Django's built-in)
class CustomPasswordResetView(PasswordResetView):
    template_name = "reset_password.html"

@login_required
def edit_profile(request):
    # 🔥 Ensure the UserProfile exists for the user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    user_form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileForm(instance=profile)  # Use the profile variable
    password_form = CustomPasswordChangeForm(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        password_form = CustomPasswordChangeForm(request.user, request.POST)

        if 'update_profile' in request.POST:
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, "✨ Your magical profile has been updated! ✨")
                return redirect('edit_profile')

        if 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "🔐 Your enchanted passphrase has been changed!")
                return redirect('edit_profile')

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form
    })


# 🚀 Profile View with Slug Instead of Username
def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, slug=username)
    blogs = Blog.objects.filter(author=user_profile.user).order_by('-created_at')
    return render(request, 'profile.html', {'user': user_profile.user, 'blogs': blogs})
