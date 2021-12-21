def palinedromPermutation(str1):
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    even = stringEven(str1)
    characterMap = getCharacterOccurances(str1)
    numOdd, numEven = getNumOddEven(characterMap)

    if even:
        if(numOdd>0):
            return False
        else:
            return True
    else:
        if(numOdd==1):
            return True
        else:
            return False

def stringEven(str1):
    if(len(str1)%2 == 0):
        return True
    else:
        return False

def getCharacterOccurances(str1):
    characterMap = {}
    for c in str1:
        occurances = characterMap.get(c,0)
        characterMap[c] = occurances + 1
    return characterMap

def getNumOddEven(characterMap):
    numOdd = 0
    numEven = 0
    for key in characterMap:
        if characterMap[key]%2 == 0:
            numEven +=1
        else:
            numOdd += 1
    return numOdd,numEven

word1 = "tactcafaa"
result = palinedromPermutation(word1)
print(result)