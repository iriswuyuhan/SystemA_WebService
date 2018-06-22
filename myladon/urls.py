# from django.conf.urls import patterns, url

from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import ladon_view

from .service.course_webservice import Course_Service



# urlpatterns = patterns('',
#
#                        url(r'^(/.*)$', csrf_exempt(ladon_view)),
#
#                        )


urlpatterns = [
    url(r'^(/.*)$', csrf_exempt(ladon_view)),
    url(r'^course/select/$', Course_Service.select),
    url(r'^course/drop/$', Course_Service.drop),
]