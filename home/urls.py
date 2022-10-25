from django.urls import path
from . import views
urlpatterns = [
    path('',views.form,name='form'),
    path('add',views.add,name='add'),
    path('deletet/<int:id>/',views.deletet,name='deletetask'),
    path('deleteu', views.deleteu, name="deleteuser"),
    path('update/<int:id>/', views.update, name="update")
]
