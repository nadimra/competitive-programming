# pale ple -> all key values are 0 except 1
# pales pale -> all key values are 0 except 1
# pale bale -> all key values are 0, except 2, where one is +1 and the other is -1
# pale bake -> all key values are 0, except 4, where two is +1 and the other two is -1

def oneAway(str1,str2):
    characterMap = {}
    characterMap = getCharacterOccurances(characterMap,str1,True)
    characterMap = getCharacterOccurances(characterMap,str2,False)
    
    numNotZero = 0
    numOnes = 0
    numNegativeOnes = 0
    for key in characterMap:
        if characterMap[key] != 0:
            numNotZero+=1
        if characterMap[key] ==1:
            numOnes +=1
        if characterMap[key] ==-1:
            numNegativeOnes +=1
    
    if numNotZero <= 1:
        return True
    elif numNotZero == 2:
        if numOnes == numNegativeOnes:
            return True
        else: 
            return False
    else:
        return False


def getCharacterOccurances(characterMap,str1,add):
    for c in str1:
        occurances = characterMap.get(c,0)
        if add:
            characterMap[c] = occurances + 1
        else:
            characterMap[c] = occurances - 1
    return characterMap

word1 = "pale"
word2 = "lles"
result = oneAway(word1,word2)
print(result)