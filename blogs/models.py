from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=255, help_text="The enchanted title of the blog")
    slug = models.SlugField(unique=True, blank=True, help_text="The mystical identifier for this blog")
    content = models.TextField(help_text="Ancient scroll containing the blog wisdom")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wizard_blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)
    tech_stack = models.CharField(max_length=255, blank=True, null=True, help_text="The enchanted technologies used")
    tags = models.ManyToManyField('Tag', blank=True, related_name='blogs')

    # 🔥 Add category field
    category = models.CharField(max_length=100, blank=True, null=True, help_text="The arcane category of the blog")

    class Meta:
        ordering = ['-created_at']  # Latest blogs appear first

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - Written by {self.author.username}"

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='blog_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_spellcasters")  # 🧙‍♂️ Magic-related name
    content = models.TextField(help_text="Speak your incantation (comment)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"🧙‍♂️ {self.user.username} casts a spell on {self.blog.title}"
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Mystical category of the blog")

    def __str__(self):
        return self.name
