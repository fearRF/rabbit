from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from . import forms


def home(request):
    return render(request, "rabbit/home.html")


def sign_up(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = forms.RegisterForm()

    return render(request, "registration/sign-up.html", {"form": form})
