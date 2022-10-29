from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('taskdisp',views.main,name='main'),
    path('profile',views.profile,name='profile'),
    path('add',views.add,name='add'),
    path('deletet/<int:id>/',views.deletet,name='deletetask'),
    # path('deleteu', views.deleteu, name="deleteuser"),
    path('update/<int:id>/', views.update, name="update")
]
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                              
