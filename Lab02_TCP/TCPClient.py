from socket import *
HOST = '127.0.0.1'
PORT = 12000

# set up the tcp socket
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))

while (True):
    s = input("Message: ")

    if s[0:2] == "GET"
        filename = s[4:]
        f = open(filename, 'wb')
        inp = sock.recv()
        f.write(inp)

    elif s[0:2] == "PUT":
        filename = s[2:]
        f = open(filename, "r")
        d = f.read()
        sock.send(d)

    sock.sendall(s.encode("utf-8"))
    data = sock.recv(1024).decode("utf-8")

    if data == "QUIT":
        break

    if s[0:4] == "CLOSE":
        sock.close()

    print ("Received: ", data)
sock.close()
