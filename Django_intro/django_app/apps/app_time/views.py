from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# from models import *

# Create your views here.
def test(request):
    context = {"email": "blog@gmail.com", "name": "mike"}
    return render(request, "app_time/index.html", context)


def create(request):
    if request.method == "POST":
        print("*" * 50)
        print(request.POST)
        print(request.POST["name"])
        print(request.POST["desc"])
        request.session["name"] = "test"  # more on session below
        print("*" * 50)
        return redirect("/")
    else:
        return redirect("/")
