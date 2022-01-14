def binaryToString(num):
    currentString = '.'
    if num<0 or num>1:
        return "Error"

    while num>0:
        if len(currentString)>32:
            return "Error"
        else:
            r = num*2
            if r>=1:
                currentString += '1'
                num = r-1
            else:
                currentString += '0'
                num = r

    return currentString

print(binaryToString(0.3))