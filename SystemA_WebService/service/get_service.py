import xml.dom.minidom as dm

from django.http import HttpResponse

from myladon.data.Course import Course

import urllib.parse
import urllib.request

from ..constants import host

from suds.client import Client

#给管理员使用的
def getAll(request):
    course = Course()
    courseInfo = course.getCourse()
    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        c = doc.createElement("a:课程")
        cid = doc.createElement("a:课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        c.appendChild(cid)
        cnm = doc.createElement("a:课程名称")
        cnm.appendChild(doc.createTextNode(item[1]))
        c.appendChild(cnm)
        credit = doc.createElement("a:学分")
        credit.appendChild(doc.createTextNode(item[2]))
        c.appendChild(credit)
        tnm = doc.createElement("a:授课老师")
        tnm.appendChild(doc.createTextNode(item[3]))
        c.appendChild(tnm)
        croom = doc.createElement("a:授课地点")
        croom.appendChild(doc.createTextNode(item[4]))
        c.appendChild(croom)
        share = doc.createElement("a:共享")
        share.appendChild(doc.createTextNode(item[5]))
        c.appendChild(share)
        root.appendChild(c)
    doc.appendChild(root)
    return HttpResponse(doc.toxml(),"text/xml")

def getStudentCourse(request):
    sid=str(request.GET.get("sid"))
    course = Course()
    courseInfo = course.getCourse()
    stuCourseInfo = course.getSelectCourse(sid)
    for i in range(0,len(courseInfo)):
        courseInfo[i]=list(courseInfo[i])
        courseInfo[i].append(False)
    for i in range(0,len(stuCourseInfo)):
        cid=int(stuCourseInfo[i][0][1:])
        courseInfo[cid][6]=True

    doc = dm.Document()
    root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程列表")
    attr = doc.createAttribute("xmlns:a")
    attr.value = "nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in courseInfo:
        c = doc.createElement("a:课程")
        cid = doc.createElement("a:课程编号")
        cid.appendChild(doc.createTextNode(item[0]))
        c.appendChild(cid)
        cnm = doc.createElement("a:课程名称")
        cnm.appendChild(doc.createTextNode(item[1]))
        c.appendChild(cnm)
        credit = doc.createElement("a:学分")
        credit.appendChild(doc.createTextNode(item[2]))
        c.appendChild(credit)
        tnm = doc.createElement("a:授课老师")
        tnm.appendChild(doc.createTextNode(item[3]))
        c.appendChild(tnm)
        croom = doc.createElement("a:授课地点")
        croom.appendChild(doc.createTextNode(item[4]))
        c.appendChild(croom)
        share = doc.createElement("a:共享")
        share.appendChild(doc.createTextNode(item[5]))
        c.appendChild(share)
        select=doc.createElement("a:选择")
        select.appendChild(doc.createTextNode(str(item[6])))
        c.appendChild(select)
        root.appendChild(c)
    bodydata=None
    headers = {'Content-Type': 'application/soap+xml; charset="UTF-8"'}
    client = Client(host, headers=headers, faults=False, timeout=15)
    try:
        result = client.service.getUserShareCourses(sid)
        # print result
        if result[0] == 200:
            bodydata=result[1]
    except Exception as e:
        print(e)
    doc = dm.parseString(bodydata.decode("utf-8"))
    doc.appendChild(root)
    return HttpResponse(doc.toxml(),"text/xml")

def getCrossDep(request):
    sid = request.GET.get("sid")
    dep = request.GET.get("dep")
    system = 'a'

    text = {'sid': sid, 'dep': dep, 'system': system}
    text = urllib.parse.urlencode(text)
    url = host + "api/getUserShareCourses"
    req = urllib.request.Request(url='%s%s%s' % (url, '?', text))
    res = urllib.request.urlopen(req)
    content = res.read()
    print(content.decode("utf-8"))

    doc = dm.parseString(content.decode("utf-8"))

    return HttpResponse(doc.toxml(), "text/xml")
    pass