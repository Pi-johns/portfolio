from django.contrib import admin
from .models import Project, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'updated_at', 'total_likes')
    search_fields = ('title', 'description', 'technologies')
    list_filter = ('created_at', 'updated_at')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'created_at')
    search_fields = ('user__username', 'project__title', 'content')
    list_filter = ('created_at',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)