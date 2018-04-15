from django.shortcuts import render,redirect
from chat_system.models import Message
import datetime
from announcement.models import Announcement
from admin_dashboard.models import Student_profile
from django.contrib.auth.models import Group
from courses.models import Course,Term
# Create your views here.

def student_dashboard(request):
    if request.user.is_authenticated:
        students = Group.objects.get(name="Students").user_set.all()
        for student in students:
            if request.user == student:
                messages       = Message.objects.filter(reciever__username = request.user ).filter(date=datetime.date.today())
                messages_count = Message.objects.filter(reciever__username=request.user).count()
                messages_count_today = Message.objects.filter(reciever__username=request.user).filter(date=datetime.date.today()).count()
                announcement_academic = Announcement.objects.filter(an_type='Academic').exclude(an_for='Doctors').order_by('-created')
                announcement_administrative = Announcement.objects.filter(an_type='Administrative').exclude(an_for='Doctors').order_by('-created')
                date = datetime.date.today()
                profile_info = Student_profile.objects.get(user__username=request.user)

                term = Term.objects.filter(active=True)
                if term.exists():
                    registered_courses = Term.objects.get(active=True).courses.filter(student__username=request.user).exclude(passed=True)
                else:
                    registered_courses = False
                template_name = 'student/student-dashboard.html'
                context       = {
                        'messages':messages,
                    'messages_count':messages_count,
                    'messages_count_today':messages_count_today,
                    'announcement_academic': announcement_academic,
                    'announcement_administrative': announcement_administrative,
                    'date': date,
                    'profile_info':profile_info,
                    'registered_courses':registered_courses
                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')

