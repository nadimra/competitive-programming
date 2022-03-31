

def maxAggTempChange(a):
    currentMaxAgg = 0
    for i in range(0,len(a)):
        left = sum(a[0:i+1])
        right = sum(a[i:len(a)])
        current = max(left,right)
        currentMaxAgg = max(currentMaxAgg,current)
    return currentMaxAgg

def maxAggTempChangeOptimal(a):
    preSumLeft = []
    preSumRight = []

    countLeft = 0
    for i in range(0,len(a)):
        countLeft += a[i]
        preSumLeft.append(countLeft)
    
    countRight = 0
    for i in range(len(a)-1, -1, -1):
        countRight += a[i]
        preSumRight.append(countRight)
    
    currentMaxAgg = 0
    for i in range(0,len(a)):
        left = preSumLeft[i]
        right = preSumRight[len(a)-1-i]
        current = max(left,right)
        currentMaxAgg = max(currentMaxAgg,current)
    return currentMaxAgg


print(maxAggTempChangeOptimal([-1,2,3]))