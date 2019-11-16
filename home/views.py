from django.shortcuts import render
from projects.models import Project
from home.models import Skill, WorkExperience
from django.db.models.functions import Coalesce

# Create your views here.
def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    work_experiences = WorkExperience.objects.order_by(Coalesce('startDate','endDate').desc())
    context = {
        'projects': projects,
        'skills': skills,
        'work_experiences': work_experiences
    } # Context Dictionary for HTML template
    return render(request, 'home.html', context)