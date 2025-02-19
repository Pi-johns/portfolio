from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'magical_title']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-input spell-input', 'accept': 'image/*'}),
            'bio': forms.Textarea(attrs={
                'class': 'form-input spell-input', 
                'rows': 3, 
                'placeholder': '📜 Pen down your legendary tale...'
            }),
            'magical_title': forms.TextInput(attrs={
                'class': 'form-input spell-input', 
                'placeholder': '🪄 E.g., Supreme Enchanter of Django'
            }),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input spell-input', 
                'placeholder': '🧙‍♂️ Choose a wizardly name...',
                'autofocus': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input spell-input', 
                'placeholder': '📨 Enter your mystical scroll address...'
            }),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input spell-input', 
        'placeholder': '🔑 Enter your ancient passphrase...'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input spell-input', 
        'placeholder': '✨ Forge a new secret spell...'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input spell-input', 
        'placeholder': '🔮 Confirm your new incantation...'
    }))
