from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from .form import *
from .models import *
from chat_system.models import *
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.

def create_announcement(request):
    if request.user.is_authenticated:
        form = CreateAnnouncementForm(request.POST or None)
        if form.is_valid():
            an_type         = form.cleaned_data.get('an_type')
            an_for          = form.cleaned_data.get('an_for')
            an_subject      = form.cleaned_data.get('an_subject')
            an_description  = form.cleaned_data.get('an_description')
            Announcement.objects.create(
                an_type         = an_type,
                an_for          = an_for,
                an_subject      = an_subject,
                an_description  = an_description,
            )
            return redirect('announcement:create_announcement')

        announcements = Announcement.objects.all().order_by('-created')

        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()

        template_name = 'announcement/admin-add-announcement.html'
        context       = {
                    "form":form,
                    "announcements":announcements,
                    "notifications":notifications,
                    "count":count
        }
        return render(request,template_name,context)
    else:
        return redirect('accounts:login')

class UpdateAnnouncement(GroupRequiredMixin,UpdateView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
    model = Announcement
    fields = [
        'an_type',
        'an_for',
        'an_subject',
        'an_description'
    ]
    template_name = 'announcement/admin-announcement-update.html'
    success_url = reverse_lazy('announcement:create_announcement')

    def get_context_data(self, **kwargs):
        context  = super(UpdateAnnouncement,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context

class DeleteAnnouncement(GroupRequiredMixin,DeleteView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
    model = Announcement
    template_name = 'announcement/admin-announcement-delete.html'
    success_url = reverse_lazy('announcement:create_announcement')

    def get_context_data(self, **kwargs):
        context  = super(DeleteAnnouncement,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context