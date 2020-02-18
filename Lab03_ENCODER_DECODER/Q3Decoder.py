message = input("Enter the Plaintext: ")
message = message.upper()
message = message.replace(" ", "")
pss = input("Enter the Password: ")
pss = pss.upper()
ch = ''
out = ""
k = 0
for i in range(0, len(message)):
    ch = chr(ord(message[i]) - (ord(pss[k])-65))
    if ord(ch) <= 64:
            ch = chr(ord(ch)+26)
    out = out + ch
    k+=1
    if k>=len(pss):
        k = 0
print(out)