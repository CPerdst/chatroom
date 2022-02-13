from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Message(models.Model):
    message=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.user.get_full_name()