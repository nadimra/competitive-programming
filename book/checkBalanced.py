#     1
#  2     3
# 4 5   6 7 

import linkedList
import binaryTree

g = binaryTree.Graph()

nodeH = binaryTree.Node("H")
nodeG = binaryTree.Node("G")
nodeF = binaryTree.Node("F")
nodeE = binaryTree.Node("E")
nodeD = binaryTree.Node("D")
nodeC = binaryTree.Node("C")
nodeB = binaryTree.Node("B")
nodeA = binaryTree.Node("A")

nodeA.addChildLeft(nodeB)
nodeA.addChildRight(nodeC)
nodeB.addChildLeft(nodeD)
nodeD.addChildRight(nodeE)
#nodeE.addChildLeft(nodeF)
#nodeF.addChildLeft(nodeG)
#nodeF.addChildRight(nodeH)

g.addNode(nodeA)
g.addNode(nodeB)
g.addNode(nodeC)
g.addNode(nodeD)
g.addNode(nodeE)
g.addNode(nodeF)
g.addNode(nodeG)
g.addNode(nodeH)
leftHeights = []
rightHeights = []

def getHeight(node,currentHeight,direction):
    if node.children == [None,None]:
        if direction == "left":
            print(node.value)
            leftHeights.append(currentHeight)
        else:
            print(node.value)
            rightHeights.append(currentHeight)
        return
    else:
        for child in node.children:
            if child is not None:
                getHeight(child,currentHeight+1,direction)

def checkBalanced(root):
    getHeight(root.getLeftChild(),1,"left")
    getHeight(root.getRightChild(),1,"right")

    left = max(leftHeights)
    right = max(rightHeights)
    if abs(left - right)>1:
        return False
    else:
        return True 

g.displayAdjacencyList()
print(checkBalanced(nodeA))