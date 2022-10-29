from atexit import register
from django.contrib import admin
from .models import TD,USER
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .form import signin
# Register your models here.
admin.site.site_header='TO DO LIST DATABASE'
@admin.register(USER)
class userAdmin(admin.ModelAdmin):
    fields=['username','password',('first_name','last_name'),'email','gender','profile_pic','is_superuser']
    list_display = ['username','password','first_name','last_name','email','gender','profile_pic']
    search_fields=('username',)
    list_filter=['username',]

@admin.register(TD)
class TDAdmin(admin.ModelAdmin):
    list_display = ('task','task_description','num','user_id','status','start_date_time','end_date_time')
    search_fields=('task',)
    list_filter=['start_date_time',]

# admin.site.register(TD,TDAdmin)
