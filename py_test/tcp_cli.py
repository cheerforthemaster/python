from socket import *
# import time
ADDR=('localhost',22222)
tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
a=1
while(1):
    data=input('>')
    tcpCliSock.send(data.encode()*1024)
    # a=a+1
    # time.sleep(1)
tcpCliSock.close()