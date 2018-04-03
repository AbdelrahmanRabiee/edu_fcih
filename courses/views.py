from django.shortcuts import render,redirect,get_object_or_404
from chat_system.models import MessageNotification
import datetime
from .form import *
from .models import *
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import Group

# Create your views here.

'''
/******************* Courses CRUD **********************************/
'''
def add_course(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
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
            else:
                return redirect('accounts:login')
    else:
        return redirect('accounts:login')
class UpdateCourse(GroupRequiredMixin,UpdateView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')
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


class DeleteCourse(GroupRequiredMixin,DeleteView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')

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

'''
/*******************END Courses CRUD **********************************/
'''

'''
/******************* TERM CRUD **********************************/
'''
def add_term(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                form = AddTermForm(request.POST or None)
                if form.is_valid():
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
                notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
                count = MessageNotification.objects.filter(date=datetime.date.today()).count()

                template_name = 'courses/admin-add-term.html'
                context       = {
                    'form':form,
                    'termat':termat,
                    'count': count,
                    'notifications': notifications,

                }
                return render(request, template_name, context)
            else:
                return redirect('accounts:login')
    else:
        return redirect('accounts:login')

def display_courses_in_term(request,pk):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                coursez = Term.objects.get(pk=pk).courses.all().order_by('-created')
                template_name = 'courses/admin-display-courses.html'
                context = {
                    'courses':coursez
                }

                return render(request,template_name,context)
            else:
                return redirect('accounts:login')
    else:
        return redirect('accounts:login')

class UpdateTerm(GroupRequiredMixin,UpdateView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')

    model = Term
    fields = [
        'name',
        'description',
        'courses',
    ]
    template_name = 'courses/admin-term-update.html'
    success_url = reverse_lazy('courses:add_term')

    def get_context_data(self, **kwargs):
        context  = super(UpdateTerm,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context


class DeleteTerm(GroupRequiredMixin,DeleteView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')

    model = Term
    template_name = 'courses/admin-term-delete.html'
    success_url = reverse_lazy('courses:add_term')

    def get_context_data(self, **kwargs):
        context  = super(DeleteTerm,self).get_context_data(**kwargs)
        notifications = MessageNotification.objects.filter(date=datetime.date.today()).order_by('-created')
        count = MessageNotification.objects.filter(date=datetime.date.today()).count()
        context['notifications']=notifications
        context['count'] = count
        return context


'''
/******************* END TERM CRUD **********************************/
'''

'''
/************* STUDENT COURSES REGISTERATION CRUD ********************/
'''


def register_course(request):
    if request.user.is_authenticated:
        admins = Group.objects.get(name="Admins").user_set.all()
        for admin in admins:
            if request.user == admin:
                form = RegisterCourseForm(request.POST or None)
                if form.is_valid():
                    courses = form.cleaned_data.get('courses')
                    for course in courses:
                        obj = Course.objects.get(name=course)
                        print(obj.pk)
                        subject = get_object_or_404(Course, pk=obj.pk)

                        user = User.objects.get(username='20161830')
                        subject.student.add(user)
                        subject.save()

                term_courses = Term.objects.get(active=True).courses.all()

                template_name = 'courses/student-register-course.html'
                context = {
                    'term_courses':term_courses,
                    'form':form
                }
                return render(request, template_name, context)
            else:
                return redirect('accounts:login')
    else:
        return redirect('accounts:login')