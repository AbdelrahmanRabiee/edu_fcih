from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth.models import User
from .models import Student_profile,Doctor_profile
from django.contrib.auth.models import Group
from django.views.generic.edit import UpdateView,DeleteView
from chat_system.models import MessageNotification
from django.urls import reverse_lazy
import datetime
# Create your views here.


def admin_dashboard(request):
    template_name = 'super-admin/admin-dashboard.html'
    context       = {

    }

    return render(request,template_name,context)

def add_student(request):
    template_name = 'super-admin/admin-add-student.html'
    form = AddStudentForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        User.objects.create(
            username=user_name,
            password=password
        )
        student_group = Group.objects.get(name='Students')
        user          = User.objects.get(username=user_name)
        student_group.user_set.add(user)
        return redirect('admin-dashboard:add-st-profile')
    notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
    count = MessageNotification.objects.filter(date=datetime.date.today()).count()
    context       = {
            "form":form,
            'notifications':notifications,
            'count':count
    }
    return render(request,template_name,context)



def add_student_profile(request):
    template_name = 'super-admin/admin-add-student-profile.html'
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

    context = {
        "form":form,
        "queryset":queryset,
        'notifications': notifications,
        'count': count
    }
    return render(request,template_name,context)

def student_list(request):
    template_name = 'super-admin/admin-student-list.html'
    queryset = Student_profile.objects.filter(user__groups__name='Students')

    notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
    count = MessageNotification.objects.filter(date=datetime.date.today()).count()

    context ={
            "students":queryset,
        'notifications': notifications,
        'count': count

    }
    return render(request,template_name,context)


class UpdateStudentProfile(UpdateView):
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

class DeleteStudentProfile(DeleteView):
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
    template_name = 'super-admin/admin-add-doctor.html'
    form = AddDoctorForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        User.objects.create(
            username=user_name,
            password=password
        )
        doctor_group = Group.objects.get(name='Doctors')
        user          = User.objects.get(username=user_name)
        doctor_group.user_set.add(user)
        return redirect('admin-dashboard:add-doc-profile')

    notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
    count = MessageNotification.objects.filter(date=datetime.date.today()).count()

    context       = {
            "form":form,
        'notifications': notifications,
        'count': count
    }
    return render(request,template_name,context)


def add_doctor_profile(request):
    template_name = 'super-admin/admin-add-doctor-profile.html'
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

    context = {
        "form":form,
        "queryset":queryset,
        'notifications': notifications,
        'count': count
    }
    return render(request,template_name,context)

def doctor_list(request):
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


class UpdateDoctorProfile(UpdateView):
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

class DeleteDoctorProfile(DeleteView):
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
