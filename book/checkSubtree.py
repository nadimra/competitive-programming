import binaryTree

def checkSubtree(tree1,tree2):
    tree1Order = []
    tree2Order = []
    preOrder(tree1,tree1Order)
    preOrder(tree2,tree2Order)
    print(tree1Order)
    print(tree2Order)
    if isSubarray(tree1Order,tree2Order):
        return True
    else:
        return False

def preOrder(currentNode, currentOrder):
    if currentNode is None:
        currentOrder.append("X")
    else:
        currentOrder.append(str(currentNode.value))
        preOrder(currentNode.children[0],currentOrder)
        preOrder(currentNode.children[1],currentOrder)

def isSubarray(bigger,smaller):
    for i in range(0,len(bigger)):
        if bigger[i] == smaller[0]:
            j = i+1
            maxJ = j + len(smaller)-1
            while j<maxJ and bigger[j]==smaller[j-i]:
                j+=1
            if(j == maxJ):
                return True
            i = j
    return False


g = binaryTree.Graph()
nodeE = binaryTree.Node(5)
nodeD = binaryTree.Node(4)
nodeC = binaryTree.Node(3)
nodeB = binaryTree.Node(1)
nodeA = binaryTree.Node(2)
nodeA.addChildLeft(nodeB)
nodeA.addChildRight(nodeC)
nodeC.addChildLeft(nodeD)
nodeC.addChildRight(nodeE)


g2 = binaryTree.Graph()
nodeC2 = binaryTree.Node(5)
nodeB2 = binaryTree.Node(4)
nodeA2 = binaryTree.Node(3)
nodeA2.addChildLeft(nodeB2)
nodeA2.addChildRight(nodeC2)


g2.addNode(nodeA2)
g2.addNode(nodeB2)
g2.addNode(nodeC2)

currentOrder = []
print(checkSubtree(nodeA,nodeA2))


#a = [1,2,3,3,4]
#b = [1,2,3,4,5]
#print(isSubarray(b,a))