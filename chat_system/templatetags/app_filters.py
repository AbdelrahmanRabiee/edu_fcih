from django import template
register = template.Library()

from django.contrib.auth.models import User
from admin_dashboard.models import Student_profile,Doctor_profile

@register.filter(name='convert_id_sender')
def convert_id_sender(value):
    pass
    # try:
    #     user = User.objects.filter(username=value)
    #     print(value)
    # except User.DoesNotExist:
    #     user = None
    # print(user)
    # if user.exists():

        # user = User.objects.get(username=value)
        # return user.first_name + " " + user.last_name
    # try:
    #     student = Student_profile.objects.filter(user__username=value)
    #     doctor  = Doctor_profile.objects.filter(user__username=value)
    # except Student_profile.DoesNotExist:
    #     student = None
    #     doctor  = None
    #
    # if student.exists():
    #     student = Student_profile.objects.get(user=value)
    #     return student.first_name + " " + student.last_name
    #
    # if doctor.exists():
    #     doctor = Doctor_profile.objects.get(user=value)
    #     return doctor.first_name + " " + doctor.last_name


