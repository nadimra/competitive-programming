import binaryTree

# 4
# 2 6
# 1 3 5 7
g = binaryTree.Graph()

def minimalTree(numArray,low,high):
    if(high<low):
        return None

    mid = int((low+high)/2)
    newNode = binaryTree.Node(numArray[mid])
    print("added "+str(newNode.value))
    newNode.addChildLeft(minimalTree(numArray,low,mid-1))
    newNode.addChildRight(minimalTree(numArray,mid+1,high))
    g.addNode(newNode)

    return newNode



numArray = [1,2,3,4,5,6,7,8,9,10]
numArray = sorted(numArray)
minimalTree(numArray,0,len(numArray)-1)
g.displayAdjacencyList()