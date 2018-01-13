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


word = "ALPHABETIZE! THIS!"
key = [1,3,5]

word = encryptb(word,key)
print(word)
word = decryptb(word,key)
print(word)
#word = encrypta(word, key)
#print(word)
#word = decrypta(word, key)
#print(word)
