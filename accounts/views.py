from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from admin_dashboard.models import Student_profile,Doctor_profile

# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        students = Group.objects.get(name="Students").user_set.all()
        doctors = Group.objects.get(name="Doctors").user_set.all()
        for admin in admins:
            if request.user == admin:
                return redirect('admin-dashboard:admin-home')
        for student in students:
            if request.user == student:
                return redirect('student-dashboard:student-home')
        for doctor in doctors:
            if request.user == doctor:
                return redirect('doctor-dashboard:doctor-home')
    else:

        form = LoginForm(request.POST or None)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password  = form.cleaned_data.get('password')


            user = authenticate(request,username=user_name,password=password)
            if user is not None:
                login(request, user)
                admins   = Group.objects.get(name="Admins").user_set.all()
                students = Group.objects.get(name="Students").user_set.all()
                doctors = Group.objects.get(name="Doctors").user_set.all()
                for admin in admins:
                    if user == admin:
                        return redirect('admin-dashboard:admin-home')
                for student in students:
                    if user == student:
                        return redirect('student-dashboard:student-home')
                for doctor in doctors:
                    if request.user == doctor:
                        return redirect('doctor-dashboard:doctor-home')

            else:
                return redirect('accounts:login')
        template_name = 'auth/login.html'
        context = {
                "form":form,

        }
        return render(request,template_name,context)


def user_logout(request):
    logout(request)
    return redirect('accounts:login')

def index(request):
    template_name = 'index.html'
    context = {

    }
    return render(request, template_name, context)


def student_change_password(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(request.user,request.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:logout')
        else:
            messages.error(request, 'Please correct the error below.')
        profile_info = Student_profile.objects.get(user__username=request.user)
        template_name = 'auth/st_change_password.html'
        context       = {
                "form":form,
                'profile_info': profile_info
        }
        return render(request,template_name,context)
    else:
        return redirect('accounts:login')


def doctor_change_password(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(request.user,request.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:logout')
        else:
            messages.error(request, 'Please correct the error below.')
        profile_info = Doctor_profile.objects.get(user__username=request.user)
        template_name = 'auth/doc_change_password.html'
        context       = {
                "form":form,
                'profile_info': profile_info
        }
        return render(request,template_name,context)
    else:
        return redirect('accounts:login')


