from django.shortcuts import render,redirect
from .form import *
from .models import Message,MessageNotification
import datetime
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