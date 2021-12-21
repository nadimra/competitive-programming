# O(N) Approach
def checkPermutation(str1,str2):
    if(len(str1) != len(str2)):
        return False
    
    characterMapStr1 = {}
    characterMapStr2 = {}

    for c in str1:
        occurances = characterMapStr1.get(c,0)
        characterMapStr1[c] = occurances + 1

    for c in str2:
        occurances = characterMapStr2.get(c,0)
        characterMapStr2[c] = occurances + 1
    
    if characterMapStr1 == characterMapStr2:
        return True
    else:
        return False

# O(Nlogn) Approach
def checkPermutationOptimal(str1,str2):
    if(len(str1) != len(str2)):
        return False
        
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1==str2


word1 = "test"
word2 = "tset"
result = checkPermutation(word1,word2)
result2 = checkPermutationOptimal(word1,word2)

print(result)
print(result2)