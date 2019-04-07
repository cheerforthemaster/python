from tkinter import *
import tkinter
from socket import *
import time
import threading


class talk():
    udpCliSock = 0
    def __init__(self,udp):
        self.udpCliSock = udp

    def stopThread(self,root):
        self.isContinue=False
        root.quit()

    def udp_ser(self,text_msglist,text_msg,ip,Account_number,port):
        print("start thread!")
        time.sleep(1)
        addre=(ip,(int)(port))
        # 04#账号 1(发送者)#

        while(True) :
            print("sleep 3s")
            time.sleep(3)
            self.udpCliSock.sendto(("04#" + Account_number + "#").encode(), addre)
            data, addr = self.udpCliSock.recvfrom(1024)
            data = data.decode()
            data = data[3:]
            i = int(data)
            while(i>0):
                i=i-1
                self.udpCliSock.sendto(("05#"+Account_number+"#").encode(),addre)
                data, addr = self.udpCliSock.recvfrom(1024)
                data=data.decode()
                data=data.split(":")
                msgcontent = Account_number +" "+ str(data[2])+":"+str(data[3])+":"+str(data[4]) + '\n '
                text_msglist.insert(END, msgcontent, 'green')
                text_msglist.insert(END, str(data[5])+'\n')
                text_msg.delete('0.0', END)


    def udp_cli(self,ip,port,Account_number,message):
        ADDR = (ip, (int)(port))
        self.udpCliSock.sendto(message.encode(), ADDR)
        data, addr = self.udpCliSock.recvfrom(1024)
        
    # 发送按钮事件
    def sendmessage(self,text_msglist,text_msg,ip,port,Account_number):
        # 在聊天内容上方加一行 显示发送人及发送时间
        msgcontent = '我:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
        text_msglist.insert(END, msgcontent, 'green')
        str=text_msg.get('0.0', END)
        text_msglist.insert(END, str)
        str = str[:len(str)-1]
        print(str)
        message=("03#"+Account_number+"#" + str+ "#")
        self.udp_cli(ip,port,Account_number,message)
        text_msg.delete('0.0', END)



    def sendWindow(self,ip,port,Account_number):
        root = tkinter.Tk()
        root.title('与'+Account_number+'聊天中')
        # 创建几个frame作为容器
        frame_left_top = Frame(root,width=380, height=300, bg='white')
        frame_left_center = Frame(root,width=380, height=100, bg='white')
        frame_left_bottom = Frame(root,width=380, height=20)
        frame_right = Frame(root,width=170, height=400, bg='white')
        # 创建需要的几个元素
        text_msglist = tkinter.Text(frame_left_top)
        text_msg = tkinter.Text(frame_left_center)
        button_sendmsg = tkinter.Button(frame_left_bottom, text='发送', command= lambda:self.sendmessage(text_msglist,text_msg,ip,port,Account_number))
        # 创建一个绿色的tag
        text_msglist.tag_config('green', foreground='#008B00')
        # 使用grid设置各个容器位置
        frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        frame_left_center.grid(row=1, column=0, padx=2, pady=5)
        frame_left_bottom.grid(row=2, column=0)
        frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
        frame_left_top.grid_propagate(0)
        frame_left_center.grid_propagate(0)
        frame_left_bottom.grid_propagate(0)
        # 把元素填充进frame
        text_msglist.grid()
        text_msg.grid()
        button_sendmsg.grid(sticky=E)
        # 主事件循环
        # root.protocol('WM_DELETE_WINDOW', closeWindow)
        ta=threading.Thread(target=self.udp_ser,args=(text_msglist,text_msg,ip,Account_number,port))
        ta.setDaemon(True)
        ta.start()
        root.protocol('WM_DELETE_WINDOW', self.stopThread(root))
        root.mainloop()


#sendWindow('1','2','3')