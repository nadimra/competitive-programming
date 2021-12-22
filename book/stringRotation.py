def isSubstring(s1,s2):
    if str(s1) in str(s2):
        return True
    else:
        return False

def stringRotation(word1,word2):
    # Todo: check if both strings same length
    # Todo: check if strings contain same characters

    if(len(word1)!=len(word2)):
        return False

    if(sorted(word1) != sorted(word2) ):
        return False

    rotationVal = 0
    for c in range (0,len(word1)):
        newWord = word1[c]
        while isSubstring(newWord,word2) and c<len(word1)-1:
            currentWord = newWord
            newWord = currentWord + word1[c+1]
            c+=1
        rotationVal = c
        break

    subStr = word1[rotationVal::]
    if(isSubstring(subStr,word2)):
        return True
    else:
        return False



word1 = "lewaterbott"
word2 = "waterbottle"

# lewaterbott
#

result = stringRotation(word1,word2)
print(result)