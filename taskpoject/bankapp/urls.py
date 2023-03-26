from .import views
from django.urls import path

urlpatterns = [
    path('login/',views.login,name='login'),
    path('login/register/',views.Register,name='register'),
    path('login/newpage/',views.newpage,name='newpage'),
    path('login/newpage/form/',views.appform,name='appform'),
    path('login/newpage/form/logout/',views.logout,name='logout')
]