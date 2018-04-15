"""edu_fcih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import *
from django.conf.urls import include
from . import settings
from accounts.views import index
urlpatterns = [
    path('admininstrator/', admin.site.urls),
]


urlpatterns += [
        path('admin/',include('admin_dashboard.urls',namespace='admin-dashboard')),
        path('auth/',include('accounts.urls',namespace='accounts')),
        path('admin/message/',include('chat_system.urls',namespace='chat_system')),
        path('admin/announcement/',include('announcement.urls',namespace='announcement')),
        path('admin/course/',include('courses.urls',namespace='courses')),
        path('student/',include('student_dashboard.urls',namespace='student-dashboard')),
        path('doctor/',include('doctor_dashboard.urls',namespace='doctor-dashboard')),
        path('',index),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)