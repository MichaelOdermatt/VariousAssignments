message = input("Enter a Message: ")
message = message.upper()
message = message.replace(" ", "")
output = ""
ch = ''
amt = input("Shift Ammount? 0 - 25: ")
amt = int(amt)
for i in range(0, len(message)):
    ch = chr(ord(message[i])+amt)
    if ord(ch) >= 91:
        ch = chr(ord(ch)-26)
    output = output + ch
print(output)