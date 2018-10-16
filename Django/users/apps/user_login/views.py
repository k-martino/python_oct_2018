from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.core.urlresolvers import reverse
from apps.user_login.models import *


# Create your views here.
def index(request):
    return render_to_response("users_table.html")


def new(request):
    return render_to_response("new_user.html")


def edit(request):
    return render_to_response("new_user.html")


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