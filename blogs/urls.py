from django.urls import path
from .views import blog_list, blog_detail, like_blog, add_comment

urlpatterns = [
    path('', blog_list, name='blog_list'),  # 📜 Show all blogs
    path('<slug:slug>/', blog_detail, name='blog_detail'),  # 🔮 Show blog details (Uses slug)
    path('<slug:slug>/like/', like_blog, name='like_blog'),  # ⚡ Like a blog (Fixed: Uses slug)
    path('<slug:slug>/comment/', add_comment, name='add_comment'),  # ✍️ Add comment (Fixed: Uses slug)
]
