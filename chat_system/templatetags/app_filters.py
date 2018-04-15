from django import template
register = template.Library()

from django.contrib.auth.models import User
from admin_dashboard.models import Student_profile,Doctor_profile

@register.filter(name='convert_id_sender')
def convert_id_sender(value):
    try:
        student = Student_profile.objects.filter(user__username=value)
        doctor  = Doctor_profile.objects.filter(user__username=value)
    except Student_profile.DoesNotExist:
        student = None
        doctor  = None

    if student.exists():
        student = Student_profile.objects.get(user=value)
        return student.first_name + " " + student.last_name

    if doctor.exists():
        doctor = Doctor_profile.objects.get(user=value)
        return "dr. "+ doctor.first_name + " " + doctor.last_name

    if not student.exists() and not doctor.exists():
        return 'Super Admin'
