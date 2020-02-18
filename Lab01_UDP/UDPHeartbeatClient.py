import socket
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

import time
sqNum = 0;
timeStamp = time.time()

message = str(sqNum) + ' ' + str(timeStamp)

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    #sends 0, the 1, then 0 on repeat
    timeStamp = time.time()
    message = str(sqNum) + ' ' + str(timeStamp)
    #sends a string wich is 'sqNum time'
    #the string is then split by the server
    try:
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        clientSocket.settimeout(1)
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        sqNum = int(modifiedMessage)
        #print(modifiedMessage)
    except:
        print('Request Timed Out')

clientSocket.close()
