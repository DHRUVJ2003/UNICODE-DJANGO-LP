from dataclasses import fields
import imp
from django.forms import ModelForm
from .models import TD,USER
class USE(ModelForm):
    class Meta:
        model=USER
        fields=['username']
class T(ModelForm):
    class Meta:
        model=TD
        fields=['task','task_description','num','user_id','status','start_date_time','end_date_time']