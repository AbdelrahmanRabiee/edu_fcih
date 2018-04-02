from django.shortcuts import render

# Create your views here.

def student_dashboard(request):
    template_name = 'student/student-dashboard.html'
    context       = {

    }
    return render(request,template_name,context)