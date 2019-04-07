from socket import*
ADDR = ('',21568)
udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)
while(1):
    data,addr = udpSerSock.recvfrom(1024)
    print(data)
udpSerSock.close()