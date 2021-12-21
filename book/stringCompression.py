#aabccccaaa

def stringCompression(str1):
    compressedString = ""
    c = 0
    while c in range(0, len(str1)):
        originalChar = c
        counter = c+1
        currentChar = str1[originalChar]

        if(counter>= len(str1)):
            compressedString = compressedString +str1[originalChar] + str(counter-originalChar)
            break

        nextChar = str1[counter]
        while currentChar==nextChar:
            c = counter
            counter = counter+1
            if counter >= len(str1):
                break
            else:
                nextChar = str1[counter]

        compressedString = compressedString +str1[originalChar] + str(counter-originalChar)
        c+=1
    
    if(len(compressedString)>=len(str1)):
        return str1
    else:
        return compressedString

word = "accbcc"
result = stringCompression(word)
print(result)