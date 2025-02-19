from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Project, Comment
from .forms import CommentForm

# 📜 Show all mystical projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

# 🔮 Show project details & related projects
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    comments = project.project_comments.all()
    form = CommentForm()
    other_projects = Project.objects.exclude(id=project.id)[:10]  # Get other projects

    return render(request, 'project_detail.html', {
        'project': project,
        'comments': comments,
        'form': form,
        'other_projects': other_projects,
    })

# ⚡ Like a project (AJAX-powered)
def like_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user.is_authenticated:
        if project.likes.filter(id=request.user.id).exists():
            project.likes.remove(request.user)  # Unlike
            liked = False
        else:
            project.likes.add(request.user)  # Like
            liked = True
        return JsonResponse({'liked': liked, 'total_likes': project.likes.count()})
    return JsonResponse({'error': 'Login required'}, status=403)

# ✍️ Comment on a project
@login_required
def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('project_detail', project_id=project.id)
    return redirect('project_detail', project_id=project.id)
