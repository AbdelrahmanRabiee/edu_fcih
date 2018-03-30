from django.urls import path
from .views import *

app_name='announcement'
urlpatterns = [
        path('',create_announcement,name='create_announcement'),
        path('update/<int:pk>/',UpdateAnnouncement.as_view(),name='update_announcement'),
        path('delete/<int:pk>/', DeleteAnnouncement.as_view(), name='delete_announcement'),

]