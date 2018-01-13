def isInside(data, key):
    if(len(key)>len(data)):
        return -1
    count = 0
    for i in range(0,len(data)-len(key)):
        if(data[i] == key[0]):
            flag = True
            for j in range(0,len(key)):
                if(data[i+j] == key[j]):
                    continue
                else:
                    flag = False
                    break
            if(flag):
                count +=1
    return count

print(isInside("BlagblahBlaggg", "la"))
