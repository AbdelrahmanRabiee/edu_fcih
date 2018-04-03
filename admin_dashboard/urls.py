from django.urls import path
from .views import *

app_name='admin-dashboard'
urlpatterns = [
        path('',admin_dashboard,name='admin-home'),
        path('add-admin',add_admin,name='add-admin'),
        path('add-student',add_student,name='add-student'),
        path('add-st-profile',add_student_profile,name='add-st-profile'),
        path('students-list',student_list,name='students-list'),
        path('student-update/<int:pk>/',UpdateStudentProfile.as_view(),name='student-update'),
        path('student-delete/<int:pk>/', DeleteStudentProfile.as_view(), name='student-delete'),
        path('add-doctor',add_doctor,name='add-doctor'),
        path('add-doc-profile',add_doctor_profile,name='add-doc-profile'),
        path('doctors-list',doctor_list,name='doctors-list'),
        path('Doctor-update/<int:pk>/', UpdateDoctorProfile.as_view(), name='doctor-update'),
        path('doctor-delete/<int:pk>/', DeleteDoctorProfile.as_view(), name='doctor-delete'),

]