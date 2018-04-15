from django.shortcuts import render,redirect
from chat_system.models import Message
import datetime
from announcement.models import Announcement
from admin_dashboard.models import Doctor_profile
from django.contrib.auth.models import Group
# Create your views here.


def doctor_dashboard(request):
    if request.user.is_authenticated:
        doctors = Group.objects.get(name="Doctors").user_set.all()
        for doctor in doctors:
            if request.user == doctor:
                messages       = Message.objects.filter(reciever__username = request.user ).filter(date=datetime.date.today())
                messages_count = Message.objects.filter(reciever__username=request.user).count()
                messages_count_today = Message.objects.filter(reciever__username=request.user).filter(date=datetime.date.today()).count()
                announcement_academic = Announcement.objects.filter(an_type='Academic').exclude(an_for='Students').order_by('-created')
                announcement_administrative = Announcement.objects.filter(an_type='Administrative').exclude(an_for='Students').order_by('-created')
                date = datetime.date.today()
                profile_info = Doctor_profile.objects.get(user__username=request.user)

                template_name = 'doctor_dashboard/doctor-dashboard.html'
                context       = {
                        'messages':messages,
                    'messages_count':messages_count,
                    'messages_count_today':messages_count_today,
                    'announcement_academic': announcement_academic,
                    'announcement_administrative': announcement_administrative,
                    'date': date,
                    'profile_info':profile_info,

                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')

