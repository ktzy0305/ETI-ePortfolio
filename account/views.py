from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import LoginForm, RegistrationForm
from urllib.parse import urlparse

# Create your views here.
def account_login(request):
    next_url = request.GET.get('next')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next')
                if redirect_url=="None":
                    return redirect('/blog/')
                else:
                    return redirect(request.GET.get('next'))
            else:
                next_url = request.GET.get('next')
                new_context = {
                    "form": form,
                    "error": "Incorrect Username or Password!",
                    "next_url": next_url
                }
                return render(request, "account_login.html", new_context)
        else:
            next_url = request.GET.get('next')
            new_context = {
                "form": form,
                "error": "Please fill up the empty fields!",
                "next_url": next_url
            }
            return render(request, "account_login.html", new_context)
    else:
        context = {
            "form": form,
            "next_url": next_url
        }

        return render(request, "account_login.html", context)

def account_register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_context={}
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if form.check_email_exists(email):
                new_context["email_error"] = "An account with this email already exists."
            if form.check_username_exists(username):
                new_context["username_error"] = "An account with this username already exists."
            if not form.password_match(password, confirm_password):
                new_context["password_error"] = "Passwords do not match."
            if not form.is_password_strong(password):
                new_context["password_error"] = "Password must be at least 8 characters long and consist of alphabets and numbers."
            if(len(new_context)>0):
                new_context["form"] = form
                new_context["error"] = "Please correct the errors in the registration form."
                return render(request, "account_register.html", new_context)
            else:
                User.objects.create_user(username, email, confirm_password)
                return redirect('/blog/')
        else:
            print()
            new_context = {
                "form": form, 
                "error": "Please correct the errors in the registration form."
            }
            return render(request, "account_register.html", new_context)
    else:
        context = {
            "form": form
        }
        return render(request, "account_register.html", context)

def account_logout(request):
    logout(request)
    return redirect('/blog/')