from django.shortcuts import render,redirect
from chat_system.models import MessageNotification
import datetime
from .form import *
from .models import *
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


def add_course(request):

    form = AddCourseForm(request.POST or None)
    if form.is_valid():
        name                = form.cleaned_data.get('name')
        code                = form.cleaned_data.get('code')
        credit_hours        = form.cleaned_data.get('credit_hours')
        description         = form.cleaned_data.get('description')
        Course.objects.create(
            name=name,
            code=code,
            credit_hours=credit_hours,
            description=description
        )
        return redirect('courses:add_course')
    courses = Course.objects.all().order_by('id')
    notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
    count = MessageNotification.objects.filter(date=datetime.date.today()).count()
    template_name = 'courses/admin-add-subject.html'
    context       = {
        'form':form,
        'courses':courses,
        'count': count,
        'notifications': notifications,
    }
    return render(request,template_name,context)

def add_term(request):
    form = AddTermForm(request.POST or None)
    if form.is_valid():
        print("valid")
        name        = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        courses     = form.cleaned_data.get('courses')

        obj=Term.objects.create(
            name=name,
            description=description,

        )
        for course in courses:
            obj.courses.add(course)
        return redirect('courses:add_term')
    termat = Term.objects.all().order_by('-created')
    template_name = 'courses/admin-add-term.html'
    context       = {
        'form':form,
        'termat':termat,

    }
    return render(request, template_name, context)

def display_courses_in_term(request,pk):
    coursez = Term.objects.get(pk=pk).courses.all().order_by('-created')
    template_name = 'courses/admin-display-courses.html'
    context = {
        'courses':coursez
    }

    return render(request,template_name,context)



class UpdateCourse(UpdateView):
    model = Course
    fields = [
        'name',
        'code',
        'credit_hours',
        'description',
    ]
    template_name = 'courses/admin-subject-update.html'
    success_url = reverse_lazy('courses:add_course')

    def get_context_data(self, **kwargs):
        context  = super(UpdateCourse,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context


class DeleteCourse(DeleteView):
    model = Course
    template_name = 'courses/admin-subject-delete.html'
    success_url = reverse_lazy('courses:add_course')

    def get_context_data(self, **kwargs):
        context  = super(DeleteCourse,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context




