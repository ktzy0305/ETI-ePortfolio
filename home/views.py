from django.shortcuts import render
from projects.models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all() # Query
    context = {
        'projects': projects
    } # Context Dictionary for HTML template
    return render(request, 'home.html', context)