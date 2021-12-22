def rotateMatrix(mat1):
    numCol = len(mat1[0])
    numRow = len(mat1)
    rotatedMatrix = []
    for col in range(0,numCol):
        currentRow = []
        for row in range(numRow-1,-1,-1):
            currentRow.append(mat1[row][col])
        rotatedMatrix.append(currentRow)
    return rotatedMatrix

mat1 = [[0,1,2],[3,4,5],[6,7,8]]
print(mat1)
result = rotateMatrix(mat1)
print(result)