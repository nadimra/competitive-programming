import binaryTree

def firstCommonAncestor(node1,node2):
    currentNode1 = node1
    currentNode2 = node2
    while currentNode1 is not None:
        currentNode2 = node2
        while currentNode2 is not currentNode1 and currentNode2 is not None:
            currentNode2 = currentNode2.parent
        if currentNode2 is not None:
            return currentNode2
        currentNode1 = currentNode1.parent
    
    return None

g = binaryTree.Graph()

nodeJ= binaryTree.Node("J")
nodeI = binaryTree.Node("I")
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
nodeC.addChildLeft(nodeI)
nodeC.addChildRight(nodeJ)
nodeD.addChildRight(nodeE)
nodeE.addChildLeft(nodeF)
nodeF.addChildLeft(nodeG)
nodeF.addChildRight(nodeH)

nodeB.setParent(nodeA)
nodeC.setParent(nodeA)
nodeD.setParent(nodeB)
nodeE.setParent(nodeD)
nodeF.setParent(nodeE)
nodeG.setParent(nodeF)
nodeH.setParent(nodeF)
nodeI.setParent(nodeC)
nodeJ.setParent(nodeC)


g.addNode(nodeA)
g.addNode(nodeB)
g.addNode(nodeC)
g.addNode(nodeD)
g.addNode(nodeE)
g.addNode(nodeF)
g.addNode(nodeG)


print(firstCommonAncestor(nodeD,nodeI).value)