#Encryption function for Part 1a
def encrypta(string, key):
    #Convert string to a list since more easy to manipulate
    out = list(string)
    #Repeat the cipher algorithm 'key' times
    for i in range(0, key):
        #Iterate through all the letters
        for j in range(0, len(out)):
            #If the letter is not a capital letter, ignore it
            if(ord(out[j]) > 90 or ord(out[j]) < 65):
                continue
            else:
                #If the letter is a Z, change to an A
                if(ord(out[j]) == 90):
                    out[j] = chr(65)
                #If the letter anything else, just increment it by one    
                else:
                    out[j] = chr(ord(out[j])+1)
    #Convert the list of letters back into a string
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

#Decryption function for Part 1a
def decrypta(string, key):
    #Convert string to a list since more easy to manipulate
    out = list(string)
    #Repeat the cipher algorithm 'key' times
    for i in range(0, key):
        #Iterate through all the letters
        for j in range(0, len(out)):
            #If the letter is not a capital letter, ignore it
            if(ord(out[j]) > 90 or ord(out[j]) < 65):
                continue
            else:
                #If the letter is an A, roll back to a Z
                if(ord(out[j]) == 65):
                    out[j] = chr(90)
                #If the letter is anything else, decrement it by 1
                else:
                    out[j] = chr(ord(out[j])-1)
    #Convert the list of letters back into a string
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

#Encryption function for Part 1b
def encryptb(string, key):
    #Convert string to a list since more easy to manipulate
    out = list(string)
    #Initialize a counter variable as an index for the key since it is a list
    count = 0
    #Iterate throught each letter in the word
    for i in range(0,len(string)):
        #If the letter is not a capital letter, ignore it
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            #Determine the index of the key for the current letter
            #by taking the remainder of the count divided by the
            #length of the key
            keyCurrent = key[count%len(key)]##
            #Loop through the letter change 'keyCurrent'(calculated above) times
            for j in range(0, keyCurrent):
                #If character is a Z, roll back to an A
                if(ord(out[i]) == 90):
                    out[i] = chr(65)
                #Otherwise just increment character by one
                else:
                   out[i] = chr(ord(out[i])+1)
            #Increment count by one
            count +=1
    #Convert the list of letters back into a string
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

#Decryption function for Part 1b
def decryptb(string, key):
    #Convert string to a list since more easy to manipulate
    out = list(string)
    #Initialize a counter variable as an index for the key since it is a list
    count = 0
    #Iterate through each letter in the word
    for i in range(0,len(string)):
        #If the letter is not a capital letter, ignore it
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            #Determine the index of the key for the current letter
            #by taking the remainder of the count divided by the
            #length of the key
            keyCurrent = key[count%len(key)]##
            #Loop through the letter change 'keyCurrent'(calculated above) times
            for j in range(0, keyCurrent):
                #If character is a A, roll up to a Z
                if(ord(out[i]) == 65):
                    out[i] = chr(90)
                #Otherwise just increment character by one
                else:
                   out[i] = chr(ord(out[i])-1)
            #Increment count by one
            count +=1
    #Convert the list of letters back into a string
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

#Encryption function for Part 1c
def encryptc(string, key):
    #Convert string to a list since more easy to manipulate
    out = list(string)
    #Iterate through the input string
    for i in range(0,len(string)):
    #If the letter is not a capital letter, ignore it
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            #Let the index be the ASCII value of the current character, normalized to A=0
            index = ord(out[i])-65
            #Make the character at that index be equal to the character at the key
            out[i] = key[index]
    #Convert list of letters back into a string
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s


#Decryption function for Part 1c
def decryptc(string, key):
    #Convert string to a list since more easy to manipulate
    out = list(string)
    #Iterate through the input string
    for i in range(0,len(string)):
        #If the letter is not a capital letter, ignore it
        if(ord(out[i]) > 90 or ord(out[i]) < 65):
            continue
        else:
            #Let the index be the location where the current letter is found in the key
            index = key.index(out[i])
            #Make the current letter equal to the ASCII value of the index, normalized since A=65
            out[i] = chr(index+65)
    #Convert list of letters back into a string
    s = ""
    for k in range(0, len(out)):
        s += out[k]
    return s

#Function to determine whether can convert variable into an integer
def convertToInt(val):
    try:
        val = int(val)
    except ValueError:
        return -1
    return val
while(1):
    #Receive a command
    command = input().split(' | ')
    #If the first command is to encrypt:
    if(command[0] == 'ENCRYPT'):
        #If the middle command can be converted to an integer, then it is Part 1A
        if(convertToInt(command[1]) != -1):
            print(encrypta(command[2], int(command[1])))
        #If the length of the second command if 26 then is its Part 1C
        elif(len(command[1]) == 26):
            print(encryptc(command[2], command[1]))
        #Otherwise it is Part 1B, and must be split to remove extra spaces beforehand
        else:
            split = [int(x) for x in command[1].split(' ')]
            print(encryptb(command[2], split))

    #If the first command is to encrypt
    elif(command[0] == 'DECRYPT'):
        #If the middle command can be converted to an integer, then it is Part 1A
        if(convertToInt(command[1]) != -1):
            print(decrypta(command[2], int(command[1])))
        #If the length of the second command if 26 then is its Part 1C
        elif(len(command[1]) == 26):
            print(decryptc(command[2], command[1]))
        #Otherwise it is Part 1B, and must be split to remove extra spaces beforehand
        else:
            split = [int(x) for x in command[1].split(' ')]
            print(decryptb(command[2], split))








