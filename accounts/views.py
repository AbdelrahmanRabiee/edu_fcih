from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        students = Group.objects.get(name="Students").user_set.all()
        for admin in admins:
            if request.user == admin:
                return redirect('admin-dashboard:admin-home')
        for student in students:
            if request.user == student:
                return redirect('student-dashboard:student-home')
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
                for admin in admins:
                    if user == admin:
                        return redirect('admin-dashboard:admin-home')
                for student in students:
                    if user == student:
                        return redirect('student-dashboard:student-home')
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