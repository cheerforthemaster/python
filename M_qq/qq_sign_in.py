import tkinter
from tkinter import *
import qq_talk
from socket import *

udpCliSock = socket(AF_INET, SOCK_DGRAM)
m_talk = qq_talk.talk(udpCliSock)
class settingANDtalk(tkinter.Frame):

    def setting(self):
        self.quit_window = tkinter.Toplevel(self.master)
        self.quit_window.title("setting")
        self.quit_window.minsize(width=300, height=120)

        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        quit_label_ip = tkinter.Label(self.quit_window, text="ip:")
        quit_label_ip.grid(row=0)
        text_ip = tkinter.Entry(self.quit_window,textvariable=v1)
        text_ip.grid(row=0,column=1)
        text_ip.insert(END, "202.114.196.97")

        quit_label_port = tkinter.Label(self.quit_window, text="端口:")
        quit_label_port.grid(row=1)
        text_port = tkinter.Entry(self.quit_window,textvariable=v2)
        text_port.grid(row=1,column=1)
        text_port.insert(END, "21568")

        quit_label_Account = tkinter.Label(self.quit_window, text="好友账号:")
        quit_label_Account.grid(row=2)
        text_Account = tkinter.Entry(self.quit_window,textvariable=v3)
        text_Account.grid(row=2,column=1)
        text_Account.insert(END,"20161003361")


        yes_button = tkinter.Button(self.quit_window, text="Yes", command=lambda :self.Get(v1,v2,v3))
        yes_button.grid(row=3,column=1)
        no_button = tkinter.Button(self.quit_window, text="No", command=self.quit_window.destroy)
        no_button.grid(row=4,column=1)

    def Get(self,v1,v2,v3):
        self.ip= v1.get()
        self.port = v2.get()
        self.Account_number=v3.get()
        self.M_send()
    def Start(self):
        self.setting()
    def M_send(self):
        self.quit_window.destroy()
        #if(isLode):
        m_talk.sendWindow(self.ip, self.port, self.Account_number)



class MyApp(tkinter.Frame):

    def __init__(self, master):
        tkinter.Frame.__init__(self, master, padx=10, pady=10)
        master.title("Sample Application")
        master.minsize(width=250, height=100)
        self.grid(row=0)


        self.upButton = tkinter.Button(self, text="登陆", command=lambda :self.Land(1))
        self.upButton.grid(row=1)
        self.downButton = tkinter.Button(self, text="注册", command=lambda :self.Land(0))
        self.downButton.grid(row=1,column=1)

        self.value = 0
        self.value_str = tkinter.StringVar()
        self.value_str.set("NULL")

        self.valueLabel = tkinter.Label(self, textvariable=self.value_str)
        self.valueLabel.grid(row=3)


        self.quitButton = tkinter.Button(self, text="Quit", command=self.create_quit_window)
        self.quitButton.grid(row=4)

        preObj = settingANDtalk()

        self.quitButton1 = tkinter.Button(self, text="firend1", command=preObj.Start)
        self.quitButton1.grid(row=5)
        self.quitButton2 = tkinter.Button(self, text="firend2", command=preObj.Start)
        self.quitButton2.grid(row=5,column=1)
        self.quitButton3 = tkinter.Button(self, text="firend3", command=preObj.Start)
        self.quitButton3.grid(row=5,column=2)
        self.quitButton4 = tkinter.Button(self, text="firend4", command=preObj.Start)
        self.quitButton4.grid(row=6)
        self.quitButton11 = tkinter.Button(self, text="firend5", command=preObj.Start)
        self.quitButton11.grid(row=6,column=1)
        self.quitButton21 = tkinter.Button(self, text="firend6", command=preObj.Start)
        self.quitButton21.grid(row=6,column=2)
        self.quitButton31 = tkinter.Button(self, text="firend7", command=preObj.Start)
        self.quitButton31.grid(row=7)
        self.quitButton41 = tkinter.Button(self, text="firend8", command=preObj.Start)
        self.quitButton41.grid(row=7,column=1)
        self.quitButton41 = tkinter.Button(self, text="firend9", command=preObj.Start)
        self.quitButton41.grid(row=7,column=2)

        master.protocol('WM_DELETE_WINDOW', self.create_quit_window)
    def Land(self,Bool):
        quit_window = tkinter.Toplevel(self.master)
        quit_window.title("setting")
        quit_window.minsize(width=300, height=120)
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        quit_label_ip = tkinter.Label(quit_window, text="ip:")
        quit_label_ip.grid(row=0)
        text_ip = tkinter.Entry(quit_window, textvariable=v1)
        text_ip.grid(row=0, column=1)
        text_ip.insert(END, "202.114.196.97")

        quit_label_port = tkinter.Label(quit_window, text="端口:")
        quit_label_port.grid(row=1)
        text_port = tkinter.Entry(quit_window, textvariable=v2)
        text_port.grid(row=1, column=1)
        text_port.insert(END, "21568")

        quit_label_Account = tkinter.Label(quit_window, text="账号:")
        quit_label_Account.grid(row=2)
        text_Account = tkinter.Entry(quit_window, textvariable=v3)
        text_Account.grid(row=2, column=1)
        text_Account.insert(END,"20161003361")

        quit_label_password = tkinter.Label(quit_window, text="密码:")
        quit_label_password.grid(row=3)
        text_password = tkinter.Entry(quit_window, textvariable=v4)
        text_password.grid(row=3, column=1)
        text_password.insert(END,"cheerforthemastercheerforthemaster")

        if 1-Bool:
            quit_label_ispassword = tkinter.Label(quit_window, text="确认密码:")
            quit_label_ispassword.grid(row=4)
            text_ispassword = tkinter.Entry(quit_window, textvariable=v5)
            text_ispassword.grid(row=4, column=1)
            text_ispassword.insert(END, "cheerforthemastercheerforthemaster")


        yes_button = tkinter.Button(quit_window, text="Yes", command=lambda :self.loadMessage(v1,v2,v3,v4,v5,Bool,quit_window))
        yes_button.grid(row=5,column=1)
        no_button = tkinter.Button(quit_window, text="No", command=quit_window.destroy)
        no_button.grid(row=6,column=1)


    def loadMessage(self,v1,v2,v3,v4,v5,Bool,quit_window):

        quit_window.destroy()
        ip = v1.get()
        port = v2.get()
        Account_number = v3.get()
        password = v4.get()
        ispassword=v5.get()

        ADDR = (ip, (int)(port))
        addre = ('', (int)(port))
        if Bool:
            udpCliSock.sendto(("02#"+Account_number+"#"+password+"#").encode(), ADDR)
        else:
            udpCliSock.sendto(("01#" + Account_number + "#" + password + "#" + ispassword + "#").encode(), ADDR)
        data, addr = udpCliSock.recvfrom(1024)
        data=data.decode()
        print(data)
        self.value = data
        if(data=="02:01"):
            self.value_str.set("登录成功")
        if(data=="02:02"):
            self.value_str.set("密码错误")
        if(data=="02:03"):
            self.value_str.set("用户不存在")
        if (data=="02:04"):
            self.value_str.set("用户已登录")

        if (data=="01:01"):
            self.value_str.set("用户注册成功")
        if (data=="01:02"):
            self.value_str.set("确认密码错误")
        if (data=="01:03"):
            self.value_str.set("用户已存在")

    def create_quit_window(self):
        quitwindow = tkinter.Toplevel(self.master)
        quitwindow.title("Quit?")
        quitwindow.minsize(width=150, height=50)
        quit_label = tkinter.Label(quitwindow, text="Are you sure you want to quit?")
        quit_label.grid(row=0)
        yes_button = tkinter.Button(quitwindow, text="Yes", command=lambda :self.quit_Account_number(quitwindow))
        yes_button.grid(row=1)
        no_button = tkinter.Button(quitwindow, text="No", command=quitwindow.destroy)
        no_button.grid(row=2)

    def quit_Account_number(self,quit_window):
        ADDR = ("202.114.196.97", 21568)
        addre = ('',21568)
        udpCliSock.sendto(("06#").encode(), ADDR)
        data,ad = udpCliSock.recvfrom(1024)
        print(data.decode())
        quit_window.destroy()
        self.master.destroy()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
