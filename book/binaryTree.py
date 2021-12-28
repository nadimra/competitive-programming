class Graph:
    def __init__(self):
        self.nodes = []
    
    def addNode(self,node):
        self.nodes.append(node)

    def displayAdjacencyList(self):
        for node in self.nodes:
            print(node.value,end=": ")
            for child in node.children:
                print(child.value if child is not None else None,end=" ")
            print()

class Node:
    def __init__(self,value):
        self.value = value
        self.children = [None,None]
        self.parent = None
    
    def setParent(self,node):
        self.parent = node

    def addChildLeft(self,node):
        self.children[0] = node

    def addChildRight(self,node):
        self.children[1] = node
    
    def checkLeftChildEmpty(self):
        if self.children[0] is not None:
            return False
        else:
            return True

    def checkRightChildEmpty(self):
        if self.children[1] is not None:
            return False
        else:
            return True

    def getLeftChild(self):
        return self.children[0]

    def getRightChild(self):
        return self.children[1]
    
    def isLeaf(self):
        if self.children == [None,None]:
            return True
        else:
            return False



#numArray = [3,4,2,7,2,10,5]

#createBinarySearchTree(numArray)
