#coding:utf-8
from suds.client import Client


user_url="http://localhost:8080/services/HelloWorld?wsdl" #这里是你的webservice访问地址
client=Client(user_url)#Client里面直接放访问的URL，可以生成一个webservice对象

print(client)

t={'url':"752256693@qq.com",'payload':"1234566"}

result=client.service.sendEmail(t)

print(result)