from django.urls import path
from .views import *

app_name='chat_system'
urlpatterns = [
        path('',send_message,name='message'),



        ]