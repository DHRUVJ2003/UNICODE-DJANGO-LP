from atexit import register
from django.contrib import admin
from .models import TD,USER
# Register your models here.
@admin.register(USER)
class USERAdmin(admin.ModelAdmin):
    list_display = ('username',)
@admin.register(TD)
class TDAdmin(admin.ModelAdmin):
    list_display = ('task','task_description','num','user_id','status','start_date_time','end_date_time')