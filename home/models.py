from ctypes.wintypes import BOOLEAN
import email
from email.policy import default
import profile
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import BooleanField, CharField
from django.contrib.auth.models import (AbstractUser)
# from .manager import USERmanager
# class USERmanager(BaseUserManager):
#     def create_user(self,email):
#         if not email:
#             raise ValueError()
class USER(AbstractUser):
    gender_choices=[('M','MALE'),('F','FEMALE'),('O','OTHERS')]
    email=models.EmailField(max_length=254)
    gender=models.CharField(max_length=1,choices=gender_choices)
    profile_pic=models.ImageField(upload_to='images/',default='images/xyz.jpg')
    
    def __str__(self):
        return self.username
    
    # objects=USERmanager()
    # REQUIRED_FIELDS=[]

    # username=models.CharField(default='',primary_key=True,max_length=50)
class TD(models.Model):
    task=models.CharField(max_length=200,default='')
    task_description=models.TextField(default='')
    num=models.IntegerField()
    user=models.ForeignKey(USER, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    start_date_time=models.DateTimeField()
    end_date_time=models.DateTimeField()

    def __str__(self):
       return self.task 



