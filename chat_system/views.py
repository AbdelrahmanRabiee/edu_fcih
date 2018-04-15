from django.shortcuts import render,redirect
from .form import *
from .models import Message,MessageNotification
import datetime
from admin_dashboard.models import Student_profile,Doctor_profile
# Create your views here.

def send_message(request):
    if request.user.is_authenticated:
        form = SendMessageForm(request.POST or None)
        if form.is_valid():
            reciever_student = form.cleaned_data.get('reciever_student')
            reciever_doctor  = form.cleaned_data.get('reciever_doctor')
            message_subject  = form.cleaned_data.get('message_subject')
            message_content  = form.cleaned_data.get('message_content')
            if reciever_student:
                Message.objects.create(
                    sender          = request.user,
                    reciever        = User.objects.get(username =reciever_student),
                    message_subject = message_subject,
                    message_content = message_content
                )
            if reciever_doctor:
                Message.objects.create(
                    sender          =request.user,
                    reciever        = User.objects.get(username =reciever_doctor),
                    message_subject = message_subject,
                    message_content = message_content
                )

            return redirect('chat_system:message')
        messages = Message.objects.all().order_by('-created')
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        template_name = 'messages/message.html'
        context = {
                "form":form,
                "messages":messages,
                'count':count,
                'notifications':notifications,
        }
        return render(request,template_name,context)
    else:
        return redirect('accounts:login')


def student_send_message(request):
    if request.user.is_authenticated:
        students = Group.objects.get(name="Students").user_set.all()
        for student in students:
            if request.user == student:
                form = StudentSendMessageForm(request.POST or None)
                if form.is_valid():
                    reciever_doctor = form.cleaned_data.get('reciever_doctor')
                    message_subject = form.cleaned_data.get('message_subject')
                    message_content = form.cleaned_data.get('message_content')

                    Message.objects.create(
                        sender=request.user,
                        reciever=User.objects.get(username=reciever_doctor),
                        message_subject=message_subject,
                        message_content=message_content
                    )
                messages = Message.objects.filter(reciever__username=request.user).order_by('-created')
                messages_count_today = Message.objects.filter(reciever__username=request.user).filter(date=datetime.date.today()).count()
                profile_info = Student_profile.objects.get(user__username=request.user)

                template_name = 'messages/studen_message.html'
                context       = {
                            'form':form,
                            'messages':messages,
                            'messages_count_today':messages_count_today,
                            'profile_info':profile_info,


                }

                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')


def doctor_send_message(request):
    if request.user.is_authenticated:
        doctors = Group.objects.get(name="Doctors").user_set.all()
        for doctor in doctors:
            if request.user == doctor:
                form = DoctorSendMessageForm(request.POST or None)
                if form.is_valid():
                    reciever_student = form.cleaned_data.get('reciever_student')
                    reciever_admin  = form.cleaned_data.get('reciever_admin')
                    message_subject  = form.cleaned_data.get('message_subject')
                    message_content  = form.cleaned_data.get('message_content')
                    if reciever_student:
                        Message.objects.create(
                            sender          = request.user,
                            reciever        = User.objects.get(username =reciever_student),
                            message_subject = message_subject,
                            message_content = message_content
                        )
                    if reciever_admin:
                        Message.objects.create(
                            sender          =request.user,
                            reciever        = User.objects.get(username =reciever_admin),
                            message_subject = message_subject,
                            message_content = message_content
                        )

                    return redirect('doctor-dashboard:send-message')
                messages = Message.objects.filter(reciever__username=request.user).order_by('-created')
                messages_count_today = Message.objects.filter(reciever__username=request.user).filter(
                date=datetime.date.today()).count()
                profile_info = Doctor_profile.objects.get(user__username=request.user)
                template_name = 'messages/doctor_message.html'
                context = {
                    'form':form,
                    'messages': messages,
                    'messages_count_today': messages_count_today,
                    'profile_info': profile_info,

                }

                return render(request, template_name, context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')










