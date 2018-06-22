from .Connect import Connection
import numpy as np

class Course:
    def getCourse(self):
        conn=Connection()
        sql="SELECT * FROM dbo.课程;"
        result=conn.query(sql)
        conn.close()
        print(result)
        return result

    def getSelectCourse(self,sid):
        conn = Connection()
        sql="SELECT * FROM dbo.选课 WHERE 学生编号='"+sid+"';"
        sresult=conn.query(sql)
        conn.close()
        print(sresult)
        return sresult

    def getAllSelect(self):
        conn=Connection()
        sql="SELECT * FROM dbo.选课;"
        result=conn.query(sql)
        conn.close()
        return result

    def selectCourse(self,sid,cid):
        conn=Connection()
        sql="INSERT INTO dbo.选课 VALUES ('"+cid+"','"+sid+"',NULL);"
        try:
            conn.update(sql)
        except Exception as e:
            conn.close()
            return False
        conn.close()
        return True


    def dropCourse(self,sid,cid):
        conn=Connection()
        sql="DELETE FROM dbo.选课 WHERE 课程编号='"+cid+"' AND 学生编号='"+sid+"';"
        try:
            conn.update(sql)
        except Exception as e:
            conn.close()
            return False
        conn.close()
        return True

    def checkCourse(self,sid,cid):
        conn=Connection()
        sql = "SELECT * FROM dbo.选课 WHERE 课程编号='" + cid + "' AND 学生编号='" + sid + "';"
        result=conn.query(sql)
        conn.close()
        if result == None or len(result) == 0:
            return False
        else:
            return True

    def addCourse(self,cid,cnm,credit,teacher,croom,share):
        conn=Connection()
        sql="INSERT INTO dbo.课程 VALUES('"+cid+"','"+cnm+"','"+credit+"','"+teacher+"','"+croom+"','"+share+"');"
        try:
            conn.update(sql)
        except Exception as e:
            conn.close()
            return False
        conn.close()
        return True
        pass

    def removeCourse(self,cid):
        conn=Connection()
        sql="DELETE FROM dbo.课程 WHERE 课程编号='"+cid+"';"
        try:
            conn.update(sql)
        except Exception as e:
            conn.close()
            return False
        conn.close()
        return True