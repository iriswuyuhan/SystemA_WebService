import xml.dom.minidom as dm

from django.http import HttpResponse

from myladon.data.Course import Course

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