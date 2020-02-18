import socket

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 12000 # Port to listen on (non-privileged ports are > 1023)

# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

swt = 0;
ptime = -1;
ctime = 0;

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((HOST, 12000))

while True:
    try:
        serverSocket.settimeout(1)
        # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        # Capitalize the message from the client
        message = message.decode()

        mg2 = message.split()
        #the string of 'sqNum time' is split into the values

        #The server will send back the squence number in expects from the client
        if int(mg2[0]) == swt: #expexts sq number 1, then 0, then 1 again on repeat
            if swt == 0:
                swt = 1
            else:
                swt = 0
            message = str(swt)
        else:
            message = str(swt)
            #message is set to equal the sq number that the server expects

        if ptime == -1:# ctime stores the calculated time, ptime stores the previous time
            ptime = float(mg2[1])
            ctime = ptime
        else:
            ctime = ptime - float(mg2[1])
            ptime = float(mg2[1])
        #ctime stores the ammout of time that passes in between each packet being received

        message = message.encode()
        # If rand is less is than 4, we consider the packet lost and do not respond
        #if rand < 4:
        #    continue
        # Otherwise, the server responds
        serverSocket.sendto(message, address)
    except:
        print('Client is no longer running')
