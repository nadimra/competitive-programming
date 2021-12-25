class Graph:
    def __init__(self):
        self.nodes = []
    
    def addNode(self,node):
        self.nodes.append(node)


class Node:
    def __init__(self,name):
        self.name = name
        self.children = None
    
    def addChild(self,node):
        self.children.append(node)


