from dataclasses import fields
import imp
from django.forms import ModelForm
from .models import TD,USER
from django.contrib.auth.forms import UserCreationForm

# class USE(ModelForm):
#     class Meta:
#         model=USER
#         fields=['username']
class signin(UserCreationForm):
    class Meta:
        model=USER
        fields=['username','first_name','last_name','email','gender','profile_pic']
class T(ModelForm):
    class Meta:
        model=TD
        fields=['task','task_description','num','status','start_date_time','end_date_time']