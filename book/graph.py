class Graph:
    def __init__(self):
        self.nodes = []
    
    def addNode(self,node):
        self.nodes.append(node)

    def removeNode(self,node):
        self.nodes.remove(node)

    def displayAdjacencyList(self):
        for node in self.nodes:
            print(node.value,end=": ")
            for child in node.children:
                print(child.value if child is not None else None,end=" ")
            print()

class Node:
    def __init__(self,name):
        self.name = name
        self.children = []
    
    def addChild(self,node):
        self.children.append(node)


