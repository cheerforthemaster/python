# coding:UTF-8
import sys
import getopt
import time
import Checksum
import BasicSender

'''
This is a skeleton sender class. Create a fantastic transport protocol here.
'''
# sys.argv =[sys.argv[0],'-fREADME','-p33122','-a127.0.0.1']
class Sender(BasicSender.BasicSender):
    def __init__(self, dest, port, filename, debug=False):
        super(Sender, self).__init__(dest, port, filename, debug)

    def split_ack(self, ack):
        pieces = ack.split('|')
        return int(pieces[1])

    def handle_response(self, response_packet):
        if Checksum.validate_checksum(response_packet):
            print "recv: %s" % response_packet
            return True
        else:
            print "recv: %s <--- CHECKSUM FAILED" % response_packet
            return False

    # Main sending loop.
    def start(self):
        seqno = 0
        msg_type = None
        list_msg=[]# 储存5个包
        i=0# list_msg下标
        while not msg_type == 'end':

            msg = self.infile.read(1400)

            msg_type = 'data'
            if seqno == 0:
                msg_type = 'start'
            elif msg == "":
                msg_type = 'end'

            packet = self.make_packet(msg_type, seqno, msg)
            self.send(packet)
            # print "sent: %s" % packet

            response = self.receive(0.1)
            ischecksum=self.handle_response(response)
            while(response==None):
                self.send(packet)
                response = self.receive(0.1)
                # ischecksum = self.handle_response(response)
            ackNum=self.split_ack(response)
            if ackNum-seqno!=1:
                list_msg.append(packet)
                i+=1

            seqno += 1
            if i==5:
                while(self.split_ack(response)==self.split_packet(list_msg[0])[1]):
                    self.send(list_msg[0])
                    response=self.receive()
                ackNum=self.split_ack(response)
                # 要留下后面seqno-ackNum+1个
                list_msg=list_msg[5-(seqno-ackNum+1):]

            if msg_type == 'end' and i!=0:
                while (i!=0):
                    self.send(list_msg[0])
                    response = self.receive()
                    while (self.split_ack(response) == self.split_packet(list_msg[0])[1]):
                        self.send(list_msg[0])
                        response = self.receive()
                    i-=1

        self.infile.close()

    def handle_timeout(self):
        pass

    def handle_new_ack(self, ack):
        pass

    def handle_dup_ack(self, ack):
        pass

    def log(self, msg):
        if self.debug:
            print msg

'''
This will be run if you run this script from the command line. You should not
change any of this; the grader may rely on the behavior here to test your
submission.
'''
if __name__ == "__main__":
    def usage():
        print "BEARS-TP Sender"
        print "-f FILE | --file=FILE The file to transfer; if empty reads from STDIN"
        print "-p PORT | --port=PORT The destination port, defaults to 33122"
        print "-a ADDRESS | --address=ADDRESS The receiver address or hostname, defaults to localhost"
        print "-d | --debug Print debug messages"
        print "-h | --help Print this usage message"

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                               "f:p:a:d", ["file=", "port=", "address=", "debug="])
    except:
        usage()
        exit()

    port = 33122
    dest = "localhost"
    filename = None
    debug = False

    for o,a in opts:
        if o in ("-f", "--file="):
            filename = a
        elif o in ("-p", "--port="):
            port = int(a)
        elif o in ("-a", "--address="):
            dest = a
        elif o in ("-d", "--debug="):
            debug = True

    s = Sender(dest, port, filename, debug)
    try:
        s.start()
    except (KeyboardInterrupt, SystemExit):
        exit()
