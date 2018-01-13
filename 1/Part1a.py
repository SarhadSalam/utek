def encrypta(string, key):
    out = list(string)
    for i in range(0, key):
        for j in range(0, len(out)):
            if(ord(out[j]) > 90 or ord(out[j]) < 65):
                continue
            else:
                if(ord(out[j]) == 90):
                    out[j] = chr(65)
                else:
                    out[j] = chr(ord(out[j])+1)

    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

def decrypta(string, key):
    out = list(string)
    for i in range(0, key):
        for j in range(0, len(out)):
            if(ord(out[j]) > 90 or ord(out[j]) < 65):
                continue
            else:
                if(ord(out[j]) == 65):
                    out[j] = chr(90)
                else:
                    out[j] = chr(ord(out[j])-1)

    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

fileIn = open('1/1a.in', 'r')
fileOut = open('1/1a.out', 'w')
for line in fileIn:
    command = line.split(' | ')
    if(command[0] == 'ENCRYPT'):
            fileOut.write(encrypta(command[2], int(command[1])))
    elif(command[0] == 'DECRYPT'):
            fileOut.write(decrypta(command[2], int(command[1])))
fileIn.close()
fileOut.close()




