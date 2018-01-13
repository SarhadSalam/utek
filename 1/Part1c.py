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



word = "HELLO WORLD!"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

word = encryptc(word,key)
print(word)
word = decryptc(word,key)
print(word)
#word = encrypta(word, key)
#print(word)
#word = decrypta(word, key)
#print(word)
