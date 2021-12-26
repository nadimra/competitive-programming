import binaryTree
import bst


g = binaryTree.Graph()

"""
nodeH = binaryTree.Node(8)
nodeG = binaryTree.Node(7)
nodeF = binaryTree.Node(6)
nodeE = binaryTree.Node(5)
"""
nodeD = binaryTree.Node(10)
nodeC = binaryTree.Node(12)
nodeB = binaryTree.Node(4)
nodeA = binaryTree.Node(8)

nodeA.addChildLeft(nodeB)
nodeA.addChildRight(nodeC)
nodeC.addChildLeft(nodeD)
#nodeB.addChildLeft(nodeD)
#nodeD.addChildRight(nodeE)
#nodeE.addChildLeft(nodeF)
#nodeF.addChildLeft(nodeG)
#nodeF.addChildRight(nodeH)

g.addNode(nodeA)
g.addNode(nodeB)
g.addNode(nodeC)
"""
g.addNode(nodeD)
g.addNode(nodeE)
g.addNode(nodeF)
g.addNode(nodeG)
g.addNode(nodeH)
"""

def validateBST(root,allowableMin,allowableMax):
    if root.children == [None,None]:
        return True
    else:
        leftChild = root.children[0]
        rightChild = root.children[1]
        if leftChild is not None and rightChild is not None:
            leftCondition = leftChild.value <= root.value and leftChild.value >=allowableMin
            rightCondition = rightChild.value > root.value and rightChild.value < allowableMax
            if leftCondition and rightCondition:
                return True and validateBST(leftChild,allowableMin,root.value) and validateBST(rightChild,root.value,allowableMax)
            else:
                return False
        elif leftChild is not None:
            leftCondition = leftChild.value <= root.value and leftChild.value >=allowableMin
            if leftCondition:
                return True and validateBST(leftChild,allowableMin,root.value)
            else:
                return False
        elif rightChild is not None:
            rightCondition = rightChild.value > root.value and rightChild.value < allowableMax
            if rightCondition:
                return True and validateBST(rightChild,root.value,allowableMax)
            else:
                return False


#numArray = [3,4,2,7,2,10,5]
#g,root = bst.createBinarySearchTree(numArray)
print(validateBST(nodeA,float('-inf'),float('inf')))
