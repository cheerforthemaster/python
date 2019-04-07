from socket import *
# import threading

# def print_data(client):
#   while True:
#        data=client.recv(1024)
#        print(data)

ADDR=('',22222)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
tcpCliSock, addr = tcpSerSock.accept()
while True:
    data = tcpCliSock.recv(10)
    print(data)
    # t = threading.Thread(target=print_data,args=(tcpCliSock,))
    # t.start()
tcpCliSock.close()
tcpSerSock.close()
