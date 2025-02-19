from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.files.storage import default_storage

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True, help_text="Write your wizardly tale here")
    magical_title = models.CharField(max_length=100, blank=True, null=True, help_text="E.g., Archmage of Code, Sorcerer of Python")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # 🚀 Enhancement: Auto-update slug when username changes
        if not self.slug or self.user.username != User.objects.get(pk=self.user.pk).username:
            self.slug = slugify(self.user.username)
        
        # 🚀 Enhancement: Assign default avatar if none is uploaded
        if not self.avatar:
            self.avatar.name = "avatars/default_wizard.png"  # Make sure this image exists in your media folder

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.magical_title or 'Wandering Wizard'}"

    def get_avatar_url(self):
        """Returns the avatar URL or default if not set."""
        if self.avatar:
            return self.avatar.url
        return default_storage.url("avatars/default_wizard.png")  # Make sure default image exists
