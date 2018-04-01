from django.urls import path
from .views import *

app_name='courses'
urlpatterns = [
        path('',add_course,name='add_course'),
        path('add-term',add_term,name='add_term'),
        path('display-term-courses/<int:pk>',display_courses_in_term,name='display-courses'),
        path('course/<int:pk>/update',UpdateCourse.as_view(),name='update-course'),
        path('course/<int:pk>/delete',DeleteCourse.as_view(),name='delete-course'),

        ]