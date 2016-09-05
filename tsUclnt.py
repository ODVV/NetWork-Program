from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliServ = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('please input > ')
    if not data:
        break
    udpCliServ.sendto(data, ADDR)
    data, ADDR = udpCliServ.recvfrom(BUFSIZ)
    if not data:
        break
    print data
udpCliServ.close()

