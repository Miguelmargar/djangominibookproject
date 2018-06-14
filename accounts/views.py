from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = authenticate(username = registration_form.cleaned_data["username"], password = registration_form.cleaned_data["password1"])
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                registration_form.add_error(None, "can't log in now, try later")
            
    else:
        registration_form = UserRegistrationForm()
    
    
    return render(request, "accounts/register.html", {"form": registration_form})
    
    
def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username = login_form.cleaned_data["userlog"], password = login_form.cleaned_data["passlog"])
        
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "your username or password are incorrect")
    else:
        login_form = UserLoginForm()
        
    return render(request, "accounts/profile.html", {"form": login_form})

def profile(request):
    return render(request, "accounts/profile.html")