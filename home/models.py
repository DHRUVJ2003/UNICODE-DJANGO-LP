from ctypes.wintypes import BOOLEAN
from email.policy import default
from django.db import models
from django.forms import BooleanField, CharField
class USER(models.Model):
    username=models.CharField(default='',primary_key=True,max_length=50)
class TD(models.Model):
    task=models.CharField(max_length=200,default='')
    task_description=models.TextField(default='')
    num=models.IntegerField()
    user_id=models.ForeignKey(USER, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    start_date_time=models.DateTimeField()
    end_date_time=models.DateTimeField()




