from django.urls import path
from .views import *

app_name='accounts'
urlpatterns = [
        path('login',user_login,name='login'),
        path('logout',user_logout,name='logout'),
        path('st-change-password',student_change_password,name='st-change-password'),
        path('doc-change-password',doctor_change_password,name='doc-change-password'),


        ]