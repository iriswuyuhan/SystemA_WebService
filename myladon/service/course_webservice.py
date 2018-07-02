from ladon.ladonizer import ladonize
import xml.dom.minidom as dm
from ..data.Course import Course
from SystemA_WebService.constants import host
from suds.client import Client

class Course_Service(object):

    @ladonize(str,str,rtype=bool)
    def drop(request,sid,cid):
        success = False
        if cid[0] == 'a':
            course = Course()
            success = course.dropCourse(sid, cid)
        else:
            headers = {'Content-Type': 'application/soap+xml; charset="UTF-8"'}
            client = Client(host, headers=headers, faults=False, timeout=15)
            try:
                result = client.service.quitCourse(sid,cid)
                # print result
                if result[0] == 200:
                    success=True
                else:
                    success=False
            except Exception as e:
                success=False
        return success

    @ladonize(str,str,rtype=bool)
    def select(self,sid,cid):
        success = False
        if cid[0] == 'a':
            course = Course()
            success = course.selectCourse(sid, cid)
        else:

            headers = {'Content-Type': 'application/soap+xml; charset="UTF-8"'}
            client = Client(host, headers=headers, faults=False, timeout=15)
            try:
                result = client.service.chooseCourse(sid, cid)
                # print result
                if result[0] == 200:
                    success = True
                else:
                    success = False
            except Exception as e:
                success = False
        return success

    #outofbound
    @ladonize(str,rtype=str)
    def getStuSelect(self,sid):
        course = Course()
        stuCourseInfo = course.getSelectCourse(sid)
        wrapped = self._wrapSelect(stuCourseInfo)
        return wrapped

    @ladonize(rtype=str)
    def getAllSelect(self):
        course = Course()
        courseInfo = course.getAllSelect()
        wrapped = self._wrapSelect(courseInfo)
        return wrapped

    @ladonize(str,rtype=str)
    def getSharedCourse(self,sid):
        course = Course()
        courseInfo = course.getCourse()
        stuCourseInfo = course.getSelectCourse(sid)
        for i in range(0, len(courseInfo)):
            courseInfo[i] = list(courseInfo[i])
            courseInfo[i].append("false")
        for i in range(0, len(stuCourseInfo)):
            cid = int(stuCourseInfo[i][0][1:])
            courseInfo[cid][6] = "true"

        doc = dm.Document()
        root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程列表")
        attr = doc.createAttribute("xmlns:a")
        attr.value = "nju.edu.cn/schema/a"
        root.setAttributeNode(attr)
        for item in courseInfo:
            if item[5] == 'Y':
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
                select = doc.createElement("a:选择")
                select.appendChild(doc.createTextNode(item[6]))
                c.appendChild(select)
                root.appendChild(c)
        doc.appendChild(root)
        print(doc.toxml())
        return doc.toxml()

    def _wrapSelect(self,stuCourseInfo):
        doc = dm.Document()
        root = doc.createElementNS("nju.edu.cn/schema/a", "a:选课列表")
        attr = doc.createAttribute("xmlns:a")
        attr.value = "nju.edu.cn/schema/a"
        root.setAttributeNode(attr)
        for item in stuCourseInfo:
            select = doc.createElement("a:选课")
            dep = doc.createElement("a:开课院系")
            dep.appendChild(doc.createTextNode("A"))
            select.appendChild(dep)
            sid = doc.createElement("a:学号")
            sid.appendChild(doc.createTextNode(item[1]))
            select.appendChild(sid)
            cid = doc.createElement("a:课程编号")
            cid.appendChild(doc.createTextNode(item[0]))
            select.appendChild(cid)
            grd = doc.createElement("a:成绩")
            grd.appendChild(doc.createTextNode("无"))
            select.appendChild(grd)
            root.appendChild(select)
        doc.appendChild(root)
        return doc.toxml()

    @ladonize(str,str,rtype=bool)
    def checkSelect(self,sid,cid):
        course = Course()
        return course.checkCourse(sid, cid)

    @ladonize(rtype=str)
    def getStatistic(request):
        course = Course()
        courseInfo = course.getCourse()
        courseSelect = course.getAllSelect()
        select = []

        for i in range(0, len(courseSelect)):
            select.append(courseSelect[i][0])

        for i in range(0, len(courseInfo)):
            cid = courseInfo[i][0]
            countNum = select.count(cid)
            courseInfo[i] = list(courseInfo[i])
            courseInfo[i].append(countNum)

        doc = dm.Document()
        root = doc.createElementNS("nju.edu.cn/schema/a", "a:课程选课统计列表")
        attr = doc.createAttribute("xmlns:a")
        attr.value = "nju.edu.cn/schema/a"
        root.setAttributeNode(attr)
        for item in courseInfo:
            info = doc.createElement("a:课程选课统计")
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
            select = doc.createElement("a:选择")
            select.appendChild(doc.createTextNode(""))
            c.appendChild(select)
            num = doc.createElement("a:选课人数")
            num.appendChild(doc.createTextNode(str(item[6])))
            info.appendChild(c)
            info.appendChild(num)
            root.appendChild(info)
        doc.appendChild(root)

        return doc.toxml()
