#     2
#  3     4
# 5 6   7 8

import linkedList
import binaryTree

g = binaryTree.Graph()
listMap = {}

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
nodeE.addChildLeft(nodeF)
nodeF.addChildLeft(nodeG)
nodeF.addChildRight(nodeH)

g.addNode(nodeA)
g.addNode(nodeB)
g.addNode(nodeC)
g.addNode(nodeD)
g.addNode(nodeE)
g.addNode(nodeF)
g.addNode(nodeG)
g.addNode(nodeH)

def listOfDepths(depthLevel,root):
    if root.children == [None,None]:
        return
    else:
        for child in root.children:
            if child is not None:
                linkedListDepth = listMap.get(depthLevel,linkedList.LinkedList())
                linkedListDepth.append_node(linkedListDepth,child.value)
                listMap[depthLevel] = linkedListDepth
                listOfDepths(depthLevel+1,child)

linkedListDepth = listMap.get(0,linkedList.LinkedList())
linkedListDepth.append_node(linkedListDepth,nodeA.value)
listMap[0] = linkedListDepth
listOfDepths(1,nodeA)

for depth in listMap:
    print(depth)
    linkedListDepth = listMap[depth]
    print(linkedListDepth)
    print()
