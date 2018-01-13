def encryptc(string, key):
    out = list(string)
    for i in range(0,len(string)):
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            index = ord(out[i])-65
            out[i] = key[index]

    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s


def decryptc(string, key):
    out = list(string)
    for i in range(0,len(string)):
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            index = key.index(out[i])
            out[i] = chr(index+65)

    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s


fileIn = open('1/1c.in', 'r')
fileOut = open('1/1c.out', 'w')
for line in fileIn:
    command = line.split(' | ')
    if(command[0] == 'ENCRYPT'):
            fileOut.write(encryptc(command[2], command[1]))
    elif(command[0] == 'DECRYPT'):
            fileOut.write(decryptc(command[2], command[1]))
fileIn.close()
fileOut.close()
