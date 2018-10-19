import re

import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    @staticmethod
    def user_validator(post_data):
        errors = {}
        # Check for length
        if len(post_data["first_name"]) < 2:
            errors["first_name_len"] = "First name should have at least 2 characters"
        if len(post_data["last_name"]) < 2:
            errors["last_name_len"] = "Last name should have at least 2 characters"
        if len(post_data["alias"]) < 2:
            errors["alias_len"] = "Alias should have at least 2 characters"
        if len(post_data["email"]) < 2:
            errors["email_len"] = "Email should have at least 2 characters"
        if len(post_data["password"]) < 8:
            errors["password_len"] = "Password should have at least 8 characters"
        # Make sure names are only letters
        if not post_data["first_name"].isalpha():
            errors["first_name_alpha"] = "First name should only contain letters"
        if not post_data["last_name"].isalpha():
            errors["last_name_alpha"] = "Last name should only contain letters"
        # Make sure email matches format
        if not EMAIL_REGEX.match(post_data["email"]):
            errors["email_format"] = "Invalid email format"
        # Make sure email isn't already in the list
        if User.objects.filter(email=post_data["email"]):
            errors["email_used"] = "Email already in use"
        # Make sure both passwords match
        if post_data["pw"] != post_data["pw_confirm"]:
            errors["pw_match"] = "Passwords do not match"
        return errors

    @staticmethod
    def login_validator(post_data):
        errors = {}
        # Check if email is in the database
        if not User.objects.filter(email=post_data["email"]):
            errors["email_db_check"] = "Invalid credentials"
        # Check for correct password
        else:
            log_user = User.objects.filter(email=post_data["email"])[0]
            if not bcrypt.checkpw(post_data["pw"].encode(), log_user.password.encode()):
                errors["pw_db_check"] = "Invalid credentials"
        return errors


class BookManager(models.Manager):
    @staticmethod
    def book_validator(post_data):
        errors = {}
        # Checking for length in book title and book author
        if len(post_data["title"]) < 2:
            errors["title"] = "Title should have at least 2 characters"
        if post_data["author"] == "add":
            if len(post_data["new_author"]) < 2:
                errors["author"] = "Author name should have at least 2 characters"
        if len(post_data["review"]) < 10:
            errors["review"] = "Review should have at least 10 characters"
        return errors


class ReviewManager(models.Manager):
    @staticmethod
    def review_validator(post_data):
        errors = {}
        if len(post_data["review"]) < 2:
            errors["review"] = "Review should have at least 2 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Author(models.Model):
    name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="authored_books")
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


class Review(models.Model):
    content = models.TextField()
    reviewer = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, related_name="reviews")
    rating = models.IntegerField()
    objects = ReviewManager()
