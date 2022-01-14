def insertion(N,M,i,j):
    mask = createMask(i,j)
    clearedN = N & mask
    shiftedM = M<<i
    final = clearedN | shiftedM
    print(bin(final))
    #mask = createMask2(i,j)
    #print(bin(mask))
    #return bin(N | mask)
    pass

def createMask(i,j):
    partOne = -1 << (j+1)
    partTwo = ~(-1<<i)
    mask = partOne | partTwo
    return mask



N = 0b10000000000
M = 0b10011
i = 2
j = 6

print(insertion(N,M,i,j))