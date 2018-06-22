from django.http import HttpResponse
# from ..data.login_data import login_data
# from ..data.Course import Course
from myladon.data.login_data import login_data
from myladon.data.Course import Course
import time
import json

def login(request):
    account=request.GET.get("account")
    password=request.GET.get("password")
    return HttpResponse(login_data(account,password))
    pass

def addCourse(request):
    course=Course()
    cid="a"+str(time.strftime("%H%M%S"))
    response=json.loads(request.body.decode("utf-8"))
    cnm=response["cnm"]
    credit=response["credit"]
    teacher=response["teacher"]
    croom=response["room"]
    share=response["share"]
    return HttpResponse(course.addCourse(cid,cnm,credit,teacher,croom,share))
    pass

def removeCourse(request):
    course=Course()
    cid=request.GET.get("cid")
    return HttpResponse(course.removeCourse(cid))
    pass