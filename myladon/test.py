#encoding:utf-8
import json
# import urllib,urllib2
from suds.client import Client

# import logging
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)

# username = 'api_user'
# password = 'api_pwd'

url="http://localhost:8000/api/Course_Service/soap11/description" #接口的URL
headers = {'Content-Type': 'application/soap+xml; charset="UTF-8"'}

client = Client(url,headers=headers,faults=False,timeout=15)

def call_api_test():
    try:
        #--WSDL请求Header----------------------------------------------
        # auth = client.factory.create('AuthenticationInfo')
        # auth.userName = username
        # auth.password = password
        # client.set_options(soapheaders=auth)

        #--WSDL请求Body----------------------------------------------
        result = client.service.getStuSelect("a1")

        #print result
        if result[0] == 200:
            return (True, result[1])
        else:
            return (False, result[1])
    except Exception as e:
        return (False, e)

if __name__ == '__main__': #get_software
    a= call_api_test()
    print (a[1])