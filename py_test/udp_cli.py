from socket import *

ADDR = ('202.114.196.97', 21568)
udpCliSock = socket(AF_INET, SOCK_DGRAM)

addre = ('', 21568)

data = "02#20161003361#cheerforthemaster#"
udpCliSock.sendto(data.encode(),ADDR)
data,addr = udpCliSock.recvfrom(1024)
print(data)

data = "03#20161003361#123456#"
udpCliSock.sendto(data.encode(),ADDR)
data,addr = udpCliSock.recvfrom(1024)
print(data)

udpCliSock.close()

