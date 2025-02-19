from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q  # 🧙‍♂️ Magical query filtering
from .models import Blog, Comment, Tag
from .forms import CommentForm

# 📜 Show all mystical blogs (with search, filtering, and infinite scroll)
def blog_list(request):
    search_query = request.GET.get('search', '')
    tech_filter = request.GET.get('tech', '')
    date_filter = request.GET.get('date', '')

    # 🪄 Base query
    blogs = Blog.objects.all()

    # 🔍 Apply Filters
    if search_query:
        blogs = blogs.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    if tech_filter:
        blogs = blogs.filter(tech_stack__icontains=tech_filter)

    if date_filter:
        blogs = blogs.filter(created_at__date=date_filter)

    blogs = blogs.order_by('-created_at')  # Ensure latest blogs appear first

    # 🔄 Infinite Scroll Pagination (6 blogs per scroll)
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  # AJAX Request
        return render(request, 'partials/blog_list.html', {'blogs': page_obj})

    return render(request, 'blogs.html', {'blogs': page_obj, 'search_query': search_query, 'tech_filter': tech_filter})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.blog_comments.all()
    form = CommentForm()

    # Fetch Related Blogs
    related_blogs = Blog.objects.filter(tags__in=blog.tags.all()).exclude(id=blog.id).distinct()[:3]
    
    # Debugging
    print(f"Current Blog: {blog.title}")
    print(f"Tags: {blog.tags.all()}")
    print(f"Related Blogs: {related_blogs}")  

    return render(request, 'blog_detail.html', {
        'blog': blog, 
        'comments': comments, 
        'form': form,
        'related_blogs': related_blogs
    })
# ⚡ Like a blog (AJAX-powered)
def like_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)  # 🪄 Changed `id` to `slug`
    if request.user.is_authenticated:
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)  # Unlike
            liked = False
        else:
            blog.likes.add(request.user)  # Like
            liked = True
        return JsonResponse({'liked': liked, 'total_likes': blog.total_likes()})
    return JsonResponse({'error': 'Login required'}, status=403)

# ✍️ Comment on a blog
@login_required
def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)  # 🪄 Changed `id` to `slug`
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('blog_detail', slug=blog.slug)
    return redirect('blog_detail', slug=blog.slug)
