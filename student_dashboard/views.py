from django.shortcuts import render,redirect
from chat_system.models import Message
import datetime
from announcement.models import Announcement
from admin_dashboard.models import Student_profile
from django.contrib.auth.models import Group
# Create your views here.

def student_dashboard(request):
    if request.user.is_authenticated:
        students = Group.objects.get(name="Students").user_set.all()
        for student in students:
            if request.user == student:
                messages = Message.objects.filter(reciever__username = '20161852' ).filter(date=datetime.date.today())
                announcement_academic = Announcement.objects.filter(an_type='Academic').filter(an_for='Students').order_by('-created')
                announcement_administrative = Announcement.objects.filter(an_type='Administrative').filter(an_for='Students').order_by('-created')
                date = datetime.date.today()
                profile_info = Student_profile.objects.get(user__username='20161852')
                template_name = 'student/student-dashboard.html'
                context       = {
                        'messages':messages,
                    'announcement_academic': announcement_academic,
                    'announcement_administrative': announcement_administrative,
                    'date': date,
                    'profile_info':profile_info
                }
                return render(request,template_name,context)
            else:
                return redirect('accounts:login')
    else:
        return redirect('accounts:login')

