# O(B) time and space, not the most optimal for space


def flipBitToWin(a):
    alternatingSeq = getAlternatingSequences(a)
    return getLongestSequence(alternatingSeq)

def getLongestSequence(alternatingSeq):
    currentLongest = 0
    for i in range(0,len(alternatingSeq)):
        currentSeqLength = 0
        if(i%2 == 0):
            zeroSeq = True
        else:
            zeroSeq = False

        if(zeroSeq):
            if(alternatingSeq[i]==1):
                # merge the sequences
                if(i!=0 and i< len(alternatingSeq)-1):
                    currentSeqLength = alternatingSeq[i-1] + 1 + alternatingSeq[i+1]
                elif(i==0 and i< len(alternatingSeq)-1):
                    currentSeqLength = 1 + alternatingSeq[i+1]
                elif(i!=0 and i==len(alternatingSeq)-1):
                    currentSeqLength = alternatingSeq[i-1] + 1
            if(alternatingSeq[i]>1):
                currentSeqLength = max(1+alternatingSeq[i-1],1+alternatingSeq[i+1])
        currentLongest = max(currentSeqLength,currentLongest)
    
    return currentLongest

def getAlternatingSequences(a):
    currentSequence = []
    currentZero = True
    currentCounter = 0
    
    i=0
    while i < len(a):
        if(currentZero and a[i]!=0):
            currentSequence.append(currentCounter)
            currentCounter = 1
            currentZero = False
        elif(currentZero and a[i]==0):
            currentCounter+=1
        elif(not currentZero and a[i]!=1):
            currentSequence.append(currentCounter)
            currentCounter = 1
            currentZero = True
        elif(not currentZero and a[i]==1):
            currentCounter+=1
        i+=1

    currentSequence.append(currentCounter)
    return currentSequence


a = [1,1,0,1,1,1,0,1,1,1,1]

print(flipBitToWin(a))
