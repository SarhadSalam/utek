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

word = "ALPHABETIZE!"
key = 3

word = encrypta(word, key)
print(word)
word = decrypta(word, key)
print(word)
