from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView
from allauth.account.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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


def login_after_reset_password(request):
    url = reverse("account_login")
    return redirect(url)
