alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
file = input("File to read: ")
letter = input("Letter of Password: ")
length = input("Length of Password: ")
ch = ''
leng = 0

with open(file, "r") as fl:
    while True:
        leng = leng + 1
        ch = fl.read(1)
        if not ch:
            break
        ch = ch.upper()
        if (ord(ch)>=65) and (ord(ch)<=90):
            for i in range(0, len(alph)):
                if ch == alph[i]:
                    count[i] = count[i] + 1
for i in range(0, len(alph)):
    print(alph[i], count[i]/leng)