def zeroMatrix(mat1):
    rowMap = {}
    colMap = {}

    for row in range(0,len(mat1)):
        for col in range(0, len(mat1[0])):
            if(mat1[row][col]==0):
                rowMap[row] = 1
                colMap[col] = 1
    
    for row in range(0,len(mat1)):
        if(rowMap.get(row,0)>0):
            mat1[row] = [0]*len(mat1[0])
        for col in range(0, len(mat1[0])):
            if(colMap.get(col,0)>0):
                mat1[row][col] = 0

    print(mat1)

mat1 = [[0,1,3],[1,2,3],[3,4,3]]
zeroMatrix(mat1)