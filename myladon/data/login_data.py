from .Connect import Connection

def login_data(account,password):
    connection=Connection()
    sql="SELECT * FROM dbo.账户 WHERE 账户名='"+account+"';"
    result=connection.query(sql)
    connection.close()
    if result==None or len(result)==0:
        return False
    if result[0][1]!=password:
        return False
    else:
        return True
