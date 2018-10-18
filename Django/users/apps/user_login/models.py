from django.core.validators import MinLengthValidator, EmailValidator, MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    email_address = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(125)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # this isn't working... needed to restart shell and import again! (from apps.user_login.models import *)
    # def __repr__(self):
    #     return "<Users object: {} {} {} {}>".format(self.first_name, self.last_name, self.email_address, self.age)

    def __str__(self):
        return f"{self.first_name}"


class UserManager(models.Manager):
    def basic_validation(self, post_data):
        errors = {}
        if len(post_data['name_f'] < 3):
            errors['name_f'] = "Name must be at least 2 characters."
        return errors
