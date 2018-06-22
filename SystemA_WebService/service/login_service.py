from django.http import HttpResponse
from myladon.data.login_data import login_data

def login(request):
    account=str(request.GET.get("account"))
    password=str(request.GET.get("password"))
    valid=login_data(account,password)
    if valid:
        #get student info
        # student=Student()
        # sid=student.getSid(account)
        #get course list
        # course=Course()
        # courseInfo=course.getCourse(sid)
        # courseInfo.append(sid)
        # jsonstr=json.dumps(courseInfo)
        # return HttpResponse(jsonstr,content_type="application/json")
        print(True)
        return HttpResponse("True")
    else:
        print(False)
        return HttpResponse("False")