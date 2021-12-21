from types import DynamicClassAttribute

# O(N^2) Approach
def isUnique(str):
    passUnique = True
    for i in range(0, len(str)):
        currentChar = str[i]
        for j in range(i +1,len(str)):
            if currentChar == str[j]:
                passUnique = False

    if passUnique == True:
        return True
    else:
        return False

# O(N) Approach
def isUniqueOptimal(str):
    characterMap = {}

    for c in str:
        occurances = characterMap.get(c,0)
        if(occurances>0):
            return False
        characterMap[c] = occurances + 1

    return True




result = isUnique("test")
resultOptimal = isUniqueOptimal("test")

print(result)
print(resultOptimal)