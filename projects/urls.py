from django.urls import path
from .views import project_list, project_detail, like_project, add_comment

urlpatterns = [
    path('', project_list, name='projects'),  # 📜 Show all projects
    path('<int:project_id>/', project_detail, name='project_detail'),  # 🔮 Show project details
    path('<int:project_id>/like/', like_project, name='like_project'),  # ⚡ Like a project
    path('<int:project_id>/add_comment/', add_comment, name='add_project_comment'),
]
