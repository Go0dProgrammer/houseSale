from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    # Creating a new custom user model.
    first_name = models.CharField(max_length=50)
    sur_name = models.charFielf(max_length=50)
    email = models.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    age = models.IntegerField()
    phone = models.IntegerField()
    is_superuser = models.BooleanField(default=False)
    