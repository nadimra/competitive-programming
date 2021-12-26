import binaryTree
# if at any node, traverse right, then keen traversing left until you reach a node with no left child
# if at left leaf, the next node is the parent
# if at right leaf, the next node is the first node which traversed left
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

nodeB.setParent(nodeA)
nodeC.setParent(nodeA)
nodeD.setParent(nodeC)
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

def successor(node):
    #if there is no right subtree
    if node.children[1] is None:

        # Left leaf scenario
        if node.parent.getLeftChild() == node:
            return node.parent

        # Right leaf scenario
        currentNode = node
        while currentNode.parent is not None and currentNode != currentNode.parent.getLeftChild():
            currentNode = currentNode.parent
        if(currentNode.parent is None):
            return None
        else:
            return currentNode

    else:
        currentNode = node.children[1]
        while not currentNode.checkLeftChildEmpty():
            currentNode = currentNode.children[0]
        return currentNode

#g.displayAdjacencyList()
print(successor(nodeD).value)