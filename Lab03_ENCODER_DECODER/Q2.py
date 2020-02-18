msg = "MPHLCPESPTOPDZQXLCNS"
output = ""
ch = ''
for i in range(1, 25):
    for x in range(0, len(msg)):
        ch = chr(ord(msg[x]) + i)
        if ord(ch) >= 91:
            ch = chr(ord(ch)-26)
        output = output + ch
    print(output)
    output = ""

#the message says "beware the ides of march", the message used 15 levels of encoding