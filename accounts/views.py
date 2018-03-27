from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password  = form.cleaned_data.get('password')

        user = authenticate(request,username=user_name,password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin')
        else:
            return redirect('/')

    template_name = 'auth/login.html'
    context = {
            "form":form,
    }
    return render(request,template_name,context)


def user_logout(request):
    logout(request)

def index(request):
    template_name = 'index.html'
    context = {

    }
    return render(request, template_name, context)