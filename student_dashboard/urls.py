from django.urls import path
from .views import *
from courses.views import register_course
from chat_system.views import student_send_message

app_name='student-dashboard'
urlpatterns = [
        path('',student_dashboard,name='student-home'),
        path('register-courses',register_course,name='register-courses'),
        path('messages',student_send_message,name='send-message'),
]