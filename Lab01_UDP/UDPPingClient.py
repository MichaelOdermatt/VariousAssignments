import socket
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

lossRate = 0
minRTT = 1;
maxRTT = 0;
avgRTT = 0;

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = 'ping message'

import time

for x in range(0,10):
    try:
        t1 = time.time()
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        clientSocket.settimeout(1);

        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        t2 = time.time()

        print(modifiedMessage)

        print('RTT', t2-t1)

        if (t2-t1)>maxRTT:
            maxRTT = t2-t1

        if (t2-t1)<minRTT:
            minRTT = t2-t1

        avgRTT += t2-t1

    except:
        lossRate += 1
        print('Request Timed Out');

lossRate = lossRate/10 * 100
print('\nstats:')
print('Loss Rate = %', lossRate)
print('Max RTT =', maxRTT)
print('Min RTT =', minRTT)
print('Avg RTT =', avgRTT/10)

clientSocket.close()
