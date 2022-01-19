from django.db import models
from django.forms import PasswordInput

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=16)
    account=models.CharField(max_length=16)
    password=models.CharField(max_length=32)
    def __str__(self):
        return self.username