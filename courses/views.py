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
from django.views.generic import DetailView
from django.http import Http404
from chat_system.models import Message
from admin_dashboard.models import Student_profile

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
                    active      = form.cleaned_data.get('active')

                    obj=Term.objects.create(
                        name=name,
                        description=description,
                        active=active

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

# class DisplayCourses(DetailView):
#     template_name = 'courses/admin-display-courses.html'
#
#     def get_context_data(self, **kwargs):
#         context  = super(DisplayCourses,self).get_context_data(**kwargs)
#         return context
#
#     def get_object(self, queryset=None, **kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         instance = Course.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Sorry this item is not found !")
#
#         return instance


class UpdateTerm(GroupRequiredMixin,UpdateView):
    group_required = u"Admins"
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = reverse_lazy('accounts:login')

    model = Term
    fields = [
        'name',
        'description',
        'courses',
        'active'
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
        students = Group.objects.get(name="Students").user_set.all()
        for admin in students:
            if request.user == admin:
                term = Term.objects.filter(active=True)
                if term.exists():
                    print('term exist')
                    form = RegisterCourseForm(request.POST or None)
                    print('form exist')
                    if form.is_valid():
                        courses = form.cleaned_data.get('courses')

                        for course in courses:

                            obj = Course.objects.get(name=course)

                            subject = get_object_or_404(Course, pk=obj.pk)

                            user = User.objects.get(username=request.user)
                            subject.student.add(user)
                            subject.save()



                    messages_count_today = Message.objects.filter(reciever__username=request.user).filter(date=datetime.date.today()).count()
                    profile_info = Student_profile.objects.get(user__username=request.user)

                    template_name = 'courses/student-register-course.html'
                    context = {

                        'form':form,
                        'messages_count_today': messages_count_today,
                        'profile_info': profile_info,

                    }
                    return render(request, template_name, context)
                else:
                    return redirect('student-dashboard:student-home')

    else:
        return redirect('accounts:login')