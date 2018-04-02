from django.urls import path
from .views import *

app_name='student-dashboard'
urlpatterns = [
        path('',student_dashboard,name='student-home'),

]