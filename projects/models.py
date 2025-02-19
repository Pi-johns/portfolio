from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200, help_text="The enchanted name of the project")
    description = models.TextField(help_text="A mystical scroll detailing the project's purpose")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    technologies = models.CharField(max_length=300, help_text="Magical spells (tech stack) used")
    live_demo = models.URLField(blank=True, null=True, help_text="Portal to the live project")
    source_code = models.URLField(blank=True, null=True, help_text="Ancient scroll of source code")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wizard_projects')
    likes = models.ManyToManyField(User, related_name='liked_projects', blank=True)

    class Meta:
        ordering = ['-created_at']  # 🕰️ Show newest projects first

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()  # 🔥 Added comment count method

    def __str__(self):
        return f"{self.title} - Crafted by {self.owner.username}"

class Comment(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_spellcasters")  # 🧙‍♂️ Magic-related name
    content = models.TextField(help_text="Etch your arcane wisdom here (comment)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # 🔮 Show the latest spells (comments) first

    def __str__(self):
        return f"🧙‍♂️ {self.user.username} inscribes a rune on {self.project.title}"
