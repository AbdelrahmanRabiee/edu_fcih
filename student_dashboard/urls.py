from django.urls import path
from .views import *
from courses.views import register_course
app_name='student-dashboard'
urlpatterns = [
        path('',student_dashboard,name='student-home'),
        path('register-courses',register_course,name='register-courses'),
]