from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')




def about(request):
    # GitHub Username
    GITHUB_USERNAME = "Pi-johns"

    # GitHub API URLs
    profile_url = f"https://api.github.com/users/Pi-johns"
    repos_url = f"https://api.github.com/users/Pi-johns/repos"

    # Fetch GitHub Profile Data
    profile_response = requests.get(profile_url)
    repos_response = requests.get(repos_url)

    github_profile = profile_response.json() if profile_response.status_code == 200 else {}
    github_repos = repos_response.json() if repos_response.status_code == 200 else []

    # Skills Dictionary (Customize your skill levels)
    skills = {
        "Python": 95,
        "Django": 90,
        "JavaScript": 85,
        "React": 80,
        "PostgreSQL": 75,
        "HTML & CSS": 90,
        "Tailwind CSS": 85,
        "Bootstrap": 80,
        "Celery": 70,
        "Redis": 65,
        "GraphQL": 60,
        "Docker": 75,
        "Linux": 85,
        "Git & GitHub": 95
    }

    context = {
        "github_profile": github_profile,
        "github_repos": github_repos[:6],  # Show only the latest 6 repos
        "skills": skills,
    }

    return render(request, "about.html", context)


def contact(request):
    return render(request, 'contact.html')




