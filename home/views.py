from django.shortcuts import render
from projects.models import Project
from home.models import *
from django.db.models.functions import Coalesce
from home.forms import ContactForm
import re

# Create your views here.
def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    work_experiences = WorkExperience.objects.order_by(Coalesce('startDate','endDate').desc())
    contactForm = ContactForm()
    context = {
        'contact_form' : contactForm,
        'form_submit_success' : False,
        'projects': projects,
        'skills': skills,
        'work_experiences': work_experiences
    } # Context Dictionary for HTML template
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            print("Form Valid")
            name = contactForm.cleaned_data["name"]
            email = ""
            try:
                email = contactForm.cleaned_data["email"]
            except TypeError:
                context["email_error"] = "Invalid email format!"
            message = contactForm.cleaned_data["message"]
            if name is None:
                context["name_error"] = "Name cannot be empty!"
            elif len(name) > 50:
                context["name_error"] = "Name cannot be longer than 50 characters!"
            if email is None:
                context["email_error"] = "Email cannot be empty!"
            elif len(email) > 70:
                context["email_error"] = "Email cannot be longer than 70 characters!" 
            elif not re.match(r'', email):
                context["email_error"] = "Invalid email format!"
            if message is None:
                context["message_error"] = "Message cannot be empty!"
            elif len(message) > 2000: 
                context["message_error"] = "Message cannot be longer than 2000 characters!"
            if len(context) <= 5:
                context["form_submit_success"] = True
                contactMessage = ContactMessage(sender_name = name, sender_email = email, message = message)
                contactMessage.save()

        else:
            print("Form Invalid")
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            print(name)
            print(email)
            print(message)
            if name == "":
                context["name_error"] = "Name cannot be empty!"
            elif len(name) > 50:
                context["name_error"] = "Name cannot be longer than 50 characters!"
            if email == "":
                context["email_error"] = "Email cannot be empty!"
            elif len(email) > 70:
                context["email_error"] = "Email cannot be longer than 70 characters!" 
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                context["email_error"] = "Invalid email format!"
            if message == "":
                context["message_error"] = "Message cannot be empty!"
            elif len(message) > 2000: 
                context["message_error"] = "Message cannot be longer than 2000 characters!"
    return render(request, 'home.html', context)