from django.urls import path
from .views import *
from chat_system.views import doctor_send_message
app_name='doctor-dashboard'
urlpatterns = [
        path('',doctor_dashboard,name='doctor-home'),
        path('messages',doctor_send_message,name='send-message'),



        ]