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
def convertToInt(val):
    try:
        val = int(val)
    except ValueError:
        return -1
    return val
while(1):
    command = input().split(' | ')
    if(command[0] == 'ENCRYPT'):
        if(convertToInt(command[1]) != -1):
            print(encrypta(command[2], int(command[1])))
        elif(len(command[1]) == 26):
            print(encryptc(command[2], command[1]))
        else:
            split = [int(x) for x in command[1].split(' ')]
            print(encryptb(command[2], split))
    elif(command[0] == 'DECRYPT'):
        if(convertToInt(command[1]) != -1):
            print(decrypta(command[2], int(command[1])))
        elif(len(command[1]) == 26):
            print(decryptc(command[2], command[1]))
        else:
            split = [int(x) for x in command[1].split(' ')]
            print(decryptb(command[2], split))








