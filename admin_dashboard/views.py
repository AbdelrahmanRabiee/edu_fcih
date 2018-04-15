from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth.models import User
from .models import Student_profile,Doctor_profile
from django.contrib.auth.models import Group
from django.views.generic.edit import UpdateView,DeleteView
from chat_system.models import MessageNotification,Message
from django.urls import reverse_lazy
import datetime
from announcement.models import Announcement
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.


def admin_dashboard(request):
    if request.user.is_authenticated:
        admins             = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                students_count     = Group.objects.get(name="Students").user_set.all().count
                doctors_count      = Group.objects.get(name="Doctors").user_set.all().count
                announcement_count = Announcement.objects.all().count()
                announcement_academic = Announcement.objects.filter(an_type='Academic').order_by('-created')
                announcement_administrative = Announcement.objects.filter(an_type='Administrative').order_by('-created')
                message_count = Message.objects.all().count()
                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()
                date = datetime.date.today()
                template_name = 'super-admin/admin-dashboard.html'
                context       = {
                            'students_count':students_count,
                            'doctors_count':doctors_count,
                            'announcement_count':announcement_count,
                            'message_count':message_count,
                            'notifications': notifications,
                            'count': count,
                            'announcement_academic':announcement_academic,
                            'announcement_administrative':announcement_administrative,
                            'date':date,
                }

                return render(request,template_name,context)
        else:
            return redirect('accounts:login')
    else:
        return redirect('accounts:login')

def add_admin(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                form = AddAdminForm(request.POST or None)
                if form.is_valid():
                    user_name   = form.cleaned_data.get('user_name')
                    first_name  = form.cleaned_data.get('first_name')
                    last_name   = form.cleaned_data.get('last_name')
                    email       = form.cleaned_data.get('email')
                    password    = form.cleaned_data.get('password')

                    obj = User.objects.create_superuser(
                        username    =user_name,
                        email       =email,
                        first_name  = first_name,
                        last_name   = last_name,
                        password    = password
                    )
                    admin_group = Group.objects.get(name='Admins')
                    user = User.objects.get(username=user_name)
                    admin_group.user_set.add(user)
                    return redirect('admin-dashboard:admin-home')

                template_name = 'super-admin/admin-add-admin.html'
                context = {
                        'form':form,
                }
                return render(request,template_name,context)

        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')


def add_student(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                form = AddStudentForm(request.POST or None)
                if form.is_valid():
                    user_name = form.cleaned_data.get('user_name')
                    password  = form.cleaned_data.get('password')
                    User.objects.create_user(
                        username=user_name,
                        password=password
                    )
                    student_group = Group.objects.get(name='Students')
                    user          = User.objects.get(username=user_name)
                    student_group.user_set.add(user)
                    return redirect('admin-dashboard:add-st-profile')
                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()
                template_name = 'super-admin/admin-add-student.html'
                context       = {
                        "form":form,
                        'notifications':notifications,
                        'count':count
                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')


    else:
        return redirect('accounts:login')



def add_student_profile(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                queryset   = Group.objects.get(name="Students").user_set.all().order_by('-id')
                form = AddStudentProfileForm(request.POST or None,request.FILES)
                img = None
                if request.FILES:
                    img = request.FILES['img']
                if form.is_valid():

                    user_name   = form.cleaned_data.get('user_name')
                    first_name  = form.cleaned_data.get('first_name')
                    last_name   = form.cleaned_data.get('last_name')
                    gender      = form.cleaned_data.get('gender')
                    date_birth  = form.cleaned_data.get('date_birth')
                    phone       = form.cleaned_data.get('phone')
                    email       = form.cleaned_data.get('email')
                    religion    = form.cleaned_data.get('religion')
                    level       = form.cleaned_data.get('level')



                    Student_profile.objects.create(
                            user        =User.objects.get(username=user_name),
                            first_name  =first_name,
                            last_name   =last_name,
                            gender      = gender,
                            date_birth  =date_birth,
                            phone       =phone,
                            email       =email,
                            religion    = religion,
                            level       =level,
                            img         =img,
                        )

                    return redirect('admin-dashboard:add-student')

                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()
                template_name = 'super-admin/admin-add-student-profile.html'
                context = {
                    "form":form,
                    "queryset":queryset,
                    'notifications': notifications,
                    'count': count
                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')

def student_list(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                queryset = Student_profile.objects.filter(user__groups__name='Students')

                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()
                template_name = 'super-admin/admin-student-list.html'
                context ={
                        "students":queryset,
                    'notifications': notifications,
                    'count': count

                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')


class UpdateStudentProfile(GroupRequiredMixin,UpdateView):
    group_required = u"Admins"
    login_url           = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
    model = Student_profile
    fields = [
        'first_name',
        'last_name',
        'gender',
        'date_birth',
        'phone',
        'email',
        'religion',
        'level',
        'img'
    ]
    template_name = 'super-admin/admin-student-update.html'
    success_url = reverse_lazy('admin-dashboard:students-list')

    def get_context_data(self, **kwargs):
        context  = super(UpdateStudentProfile,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context

class DeleteStudentProfile(GroupRequiredMixin,DeleteView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
    model = Student_profile
    template_name = 'super-admin/admin-student-delete.html'
    success_url = reverse_lazy('admin-dashboard:students-list')

    def get_context_data(self, **kwargs):
        context  = super(DeleteStudentProfile,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context

'''
/*************************************************************************/
'''

def add_doctor(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                form = AddDoctorForm(request.POST or None)
                if form.is_valid():
                    user_name = form.cleaned_data.get('user_name')
                    password = form.cleaned_data.get('password')
                    User.objects.create_user(
                        username=user_name,
                        password=password
                    )
                    doctor_group = Group.objects.get(name='Doctors')
                    user          = User.objects.get(username=user_name)
                    doctor_group.user_set.add(user)
                    return redirect('admin-dashboard:add-doc-profile')

                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()
                template_name = 'super-admin/admin-add-doctor.html'
                context       = {
                        "form":form,
                    'notifications': notifications,
                    'count': count
                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')

def add_doctor_profile(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                queryset   = Group.objects.get(name="Doctors").user_set.all().order_by('-id')
                form = AddDoctorProfileForm(request.POST or None,request.FILES)
                img = None
                if request.FILES:
                    img = request.FILES['img']
                if form.is_valid():
                    user_name           = form.cleaned_data.get('user_name')
                    first_name          = form.cleaned_data.get('first_name')
                    last_name           = form.cleaned_data.get('last_name')
                    gender              = form.cleaned_data.get('gender')
                    date_birth          = form.cleaned_data.get('date_birth')
                    phone               = form.cleaned_data.get('phone')
                    email               = form.cleaned_data.get('email')
                    religion            = form.cleaned_data.get('religion')
                    highest_degree      = form.cleaned_data.get('highest_degree')
                    university_high     = form.cleaned_data.get('university_high')
                    year_passed_high    = form.cleaned_data.get('year_passed_high')
                    gpa_high            = form.cleaned_data.get('gpa_high')
                    other_degree        = form.cleaned_data.get('other_degree')
                    university_other    = form.cleaned_data.get('university_other')
                    year_passed_other   = form.cleaned_data.get('year_passed_other')
                    gpa_other           = form.cleaned_data.get('gpa_other')

                    Doctor_profile.objects.create(
                            user            =User.objects.get(username=user_name),
                            first_name      =first_name,
                            last_name       =last_name,
                            gender          = gender,
                            date_birth      =date_birth,
                            phone           =phone,
                            email           =email,
                            religion        = religion,
                            img             =img,
                            highest_degree  =highest_degree,
                            university_high =university_high,
                            year_passed_high=year_passed_high,
                            gpa_high        =gpa_high,
                            other_degree    =other_degree,
                            university_other=university_other,
                            year_passed_other=year_passed_other,
                            gpa_other       =gpa_other,



                        )

                    return redirect('admin-dashboard:add-doctor')

                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()
                template_name = 'super-admin/admin-add-doctor-profile.html'
                context = {
                    "form":form,
                    "queryset":queryset,
                    'notifications': notifications,
                    'count': count
                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')

    else:
        return redirect('accounts:login')

def doctor_list(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                template_name = 'super-admin/admin-doctor-list.html'
                queryset = Doctor_profile.objects.filter(user__groups__name='Doctors')

                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()

                context ={
                        "doctors":queryset,
                    'notifications': notifications,
                    'count': count

                }
                return render(request,template_name,context)
        else:
            return redirect('accounts:login')


    else:
        return redirect('accounts:login')

class UpdateDoctorProfile(GroupRequiredMixin,UpdateView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
    model = Doctor_profile
    fields = [
        'first_name',
        'last_name',
        'gender',
        'date_birth',
        'phone',
        'email',
        'religion',
        'img',
        'highest_degree',
        'university_high',
        'year_passed_high',
        'gpa_high',
        'other_degree',
        'university_other',
        'year_passed_other',
        'gpa_other',




    ]
    template_name = 'super-admin/admin-doctor-update.html'
    success_url = reverse_lazy('admin-dashboard:doctors-list')

    def get_context_data(self, **kwargs):
        context  = super(UpdateDoctorProfile,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context

class DeleteDoctorProfile(GroupRequiredMixin,DeleteView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
    model = Doctor_profile
    template_name = 'super-admin/admin-doctor-delete.html'
    success_url = reverse_lazy('admin-dashboard:doctors-list')

    def get_context_data(self, **kwargs):
        context  = super(DeleteDoctorProfile,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context
