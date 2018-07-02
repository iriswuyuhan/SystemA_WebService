# from django.conf.urls import patterns, url

from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import ladon_view

from .service.course_webservice import Course_Service
from .service.student_webservice import Student_Service



# urlpatterns = patterns('',
#
#                        url(r'^(/.*)$', csrf_exempt(ladon_view)),
#
#                        )


urlpatterns = [
    url(r'^(/.*)$', csrf_exempt(ladon_view)),
    url(r'^course/select/$', Course_Service.select),
    url(r'^course/drop/$', Course_Service.drop),
    url(r'^course/getStuSelect/$',Course_Service.getStuSelect),
    url(r'^course/getAllSelect/$',Course_Service.getAllSelect),
    url(r'^course/getShare/$',Course_Service.getSharedCourse),
    url(r'^course/check/$',Course_Service.checkSelect),
    url(r'^course/statistic/$',Course_Service.getStatistic),
    url(r'^student/getAllStudent/$',Student_Service.getAllStudent),
    url(r'^student/addStu/$',Student_Service.addStuInfo)
]