from atexit import register
from django.contrib import admin
from .models import TD,USER
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .form import signin
# Register your models here.
@admin.register(USER)
class userAdmin(admin.ModelAdmin):
    list_display = ['username','password','first_name','last_name','email','gender','profile_pic']

@admin.register(TD)
class TDAdmin(admin.ModelAdmin):
    list_display = ('task','task_description','num','user_id','status','start_date_time','end_date_time')