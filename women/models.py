from django.db import models


class Women(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    info = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publ = models.BooleanField(default=True)
# Create your models here.
