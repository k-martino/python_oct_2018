from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)


def new(response):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)


def create(url):
    url = "/"
    return redirect(url)


def show(response):
    response = "Placeholder to display blog {{ number }}"
    return HttpResponse(response)


def edit(response):
    response = "Placeholder to edit blog {{ number }}"
    return HttpResponse(response)


def destroy(response):
    url = "/"
    return redirect(url)
