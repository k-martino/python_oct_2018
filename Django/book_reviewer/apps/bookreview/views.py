from django.shortcuts import render, redirect
from .models import User, Author, Book, Review
from django.contrib import messages
import bcrypt


# render
def index(request):
    return render(request, "bookreview/index.html")


def home(request):
    return render(request, "/")


def add_bk(request):
    return render(request, "/")


def bk(request):
    return render(request, "/")


def usr(request):
    return render(request, "/")


# process & redirect
def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags="signup_errors")
        return redirect("/")
    else:
        user = User.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            alias=request.POST["alias"],
            email=request.POST["email"],
            pw_hash=bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
        )
        request.session["user_id"] = user.id
        request.session["logged_in"] = True
        return redirect("bookreview:home")


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login_errors")
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST["email"])
        request.session["user_id"] = user.id
        request.session["logged_in"] = True
        return redirect("bookreview:home")


def logout(request):
    request.session.clear()
    return redirect("/")


def process_bk(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("bookreview:add_bk")
        else:
            title = request.POST["title"]
            user = User.objects.get(id=request.session["user_id"])
            rating = int(request.POST["rating"])
            if request.POST["author"] == "Other":
                author = Author.objects.create(name=request.POST("new_author"), uploaded_by=user)
            else:
                author = Author.objects.filter(name=request.POST["author"])[0]
            book = Book.objects.create(title=title, author=author, uploaded_by=user)
            Review.objects.create(
                content=request.POST["review"], reviewer=user, book=book, rating=rating
            )
            request.session["book"] = book.id
            return redirect("view_bk", book_id=book.id)


def process_rev(request):
    return redirect("/")


def destroy(request):
    return redirect("/")
