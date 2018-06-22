"""SystemA_WebService URL Configuration

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
from django.conf.urls import include,url
from myladon import urls as ladon_urls
from .service import login_service
from .service import admin_service
from .service import get_service

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api', include(ladon_urls)),
    url(r'^adminlogin/$',admin_service.login),
    url(r'^usrlogin/$', login_service.login),
    url(r'^course/add/$',admin_service.addCourse),
    url(r'^course/remove/$',admin_service.removeCourse),
    url(r'^course/getAll/$',get_service.getAll), #管理员使用
]
