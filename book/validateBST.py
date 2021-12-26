import binaryTree
import bst

"""
g = binaryTree.Graph()
nodeH = binaryTree.Node(8)
nodeG = binaryTree.Node(7)
nodeF = binaryTree.Node(6)
nodeE = binaryTree.Node(5)
nodeD = binaryTree.Node(4)
nodeC = binaryTree.Node(3)
nodeB = binaryTree.Node(2)
nodeA = binaryTree.Node(1)

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
"""

def validateBST(root):
    if root.children == [None,None]:
        return True
    else:
        leftChild = root.children[0]
        rightChild = root.children[1]
        if leftChild is not None:
            if leftChild.value <= root.value:
                return True and validateBST(leftChild)
            else:
                return False
        if rightChild is not None:
            if rightChild.value > root.value:
                return True and validateBST(rightChild)
            else:
                return False

numArray = [3,4,2,7,2,10,5]
g,root = bst.createBinarySearchTree(numArray)
print(validateBST(root))
