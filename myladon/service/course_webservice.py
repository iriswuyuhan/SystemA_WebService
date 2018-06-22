from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType
from ..data.Course import Course

class Course_Service(object):

    @ladonize(str,str,rtype=bool)
    def drop(request,sid,cid):
        success = False
        if cid[0] == 'a':
            course = Course()
            success = course.dropCourse(sid, cid)
        # else:
            # TODO 调用集成服务器服务
            # text = {'sId': sid, 'cId': cid}
            # text = urllib.parse.urlencode(text)
            # url = host + "api/quitCourse"
            # req = urllib.request.Request(url='%s%s%s' % (url, '?', text))
            # res = urllib.request.urlopen(req)
            # success = res.read()
        return success

    @ladonize(str,str,rtype=bool)
    def select(self,sid,cid):
        success = False
        if cid[0] == 'a':
            course = Course()
            success = course.selectCourse(sid, cid)
        # else:
        # TODO 调用集成服务器服务
        #     text = {'sId': sid, 'cId': cid}
        #     text = urllib.parse.urlencode(text)
        #     url = host + "api/chooseCourse"
        #     req = urllib.request.Request(url='%s%s%s' % (url, '?', text))
        #     res = urllib.request.urlopen(req)
        #     success = res.read()
        return success