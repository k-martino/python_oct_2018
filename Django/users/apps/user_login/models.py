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

    def __repr__(self):
        return "<Users object: {} {} {} {}>".format(self.first_name, self.last_name, self.email_address, self.age)
