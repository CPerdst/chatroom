import imp
from django.db import models
from login.models import User
import datetime
# Create your models here.
class Msg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    msg = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.user.username