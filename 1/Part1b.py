def encryptb(string, key):
    out = list(string)
    count = 0
    for i in range(0,len(string)):
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            keyCurrent = key[count%len(key)]##
            for j in range(0, keyCurrent):
                if(ord(out[i]) == 90):
                    out[i] = chr(65)
                else:
                   out[i] = chr(ord(out[i])+1)
                
            count +=1
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s


def decryptb(string, key):
    out = list(string)
    count = 0
    for i in range(0,len(string)):
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            keyCurrent = key[count%len(key)]##
            for j in range(0, keyCurrent):
                if(ord(out[i]) == 65):
                    out[i] = chr(90)
                else:
                   out[i] = chr(ord(out[i])-1)
                
            count +=1
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s


fileIn = open('1/1b.in', 'r')
fileOut = open('1/1b.out', 'w')
for line in fileIn:
    command = line.split(' | ')
    split = [int(x) for x in command[1].split(' ')]
    if(command[0] == 'ENCRYPT'):
            fileOut.write(encryptb(command[2], split))
    elif(command[0] == 'DECRYPT'):
            fileOut.write(decryptb(command[2], split))
fileIn.close()
fileOut.close()

