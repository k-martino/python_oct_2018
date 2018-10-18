from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.user_login.models import *


# Create your views here.
def index(request):
    # Retrieve all users from database
    users = User.objects.values().all()
    return render(request, "user_login/index.html", {'users': users})


def new(request):
    return render(request, "user_login/new_user.html")


def edit(request):
    return render(request, "user_login/edit_user.html")


def show(request):
    return None


def create(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        return redirect(reverse("users:my_show"), errors)


def destroy(request):
    return None


def update(request):
    return None
