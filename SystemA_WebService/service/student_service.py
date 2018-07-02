from django.http import HttpResponse

from myladon.data.Student import Student

import xml.dom.minidom as dm


def getStuInfo(request):
    student=Student()
    stuInfo=student.getStu(request.GET.get('account'))
    result=wrapStu(stuInfo)
    return HttpResponse(result,"text/xml")

def wrapStu(stuInfo):
    student=Student()
    doc=dm.Document()
    root=doc.createElementNS("nju.edu.cn/schema/a","a:学生列表")
    attr=doc.createAttribute("xmlns:a")
    attr.value="nju.edu.cn/schema/a"
    root.setAttributeNode(attr)
    for item in stuInfo:
        stu=doc.createElement("a:学生信息")
        sid=doc.createElement("a:学号")
        sid.appendChild(doc.createTextNode(item[0]))
        stu.appendChild(sid)
        snm=doc.createElement("a:姓名")
        snm.appendChild(doc.createTextNode(item[1]))
        stu.appendChild(snm)
        sgen=doc.createElement("a:性别")
        sgen.appendChild(doc.createTextNode(item[2]))
        stu.appendChild(sgen)
        sdep=doc.createElement("a:院系")
        sdep.appendChild(doc.createTextNode(item[3]))
        stu.appendChild(sdep)
        sacc=doc.createElement("a:账户名")
        sacc.appendChild(doc.createTextNode(item[4]))
        stu.appendChild(sacc)
        account=item[4]
        aresult=student.getAccount(account)
        spwd=doc.createElement("a:密码")
        spwd.appendChild(doc.createTextNode(aresult[0][1]))
        stu.appendChild(spwd)
        sauth=doc.createElement("a:权限")
        sauth.appendChild(doc.createTextNode(aresult[0][2]))
        stu.appendChild(sauth)
        root.appendChild(stu)
    doc.appendChild(root)
    print(doc.toxml())
    return doc.toxml()