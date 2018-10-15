from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    email_address = models.EmailField(max_length=255, unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # this isn't working... needed to restart shell and import again! (from apps.user_login.models import *)
    # def __repr__(self):
    #     return "<Users object: {} {} {} {}>".format(self.first_name, self.last_name, self.email_address, self.age)

    def __str__(self):
        return f"{self.first_name}"
