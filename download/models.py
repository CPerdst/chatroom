from django.db import models

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=0)
    download_num = models.IntegerField(default=0)
    def __str__(self):
        return self.filename