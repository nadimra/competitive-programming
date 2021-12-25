import graph

def hasPath(source,dest):
    if source == dest:
        return True
    elif source is None:
        return False
    else:
        children = source.children
        if children is not None:
            for child in children:
                return hasPath(child,dest)
        else:
            return hasPath(None,dest)



graph1 = graph.Graph()
nodeE = graph.Node("E",None)
nodeD = graph.Node("D",[nodeE])
nodeC = graph.Node("C",None)
nodeB = graph.Node("B",[nodeD])
nodeA = graph.Node("A",[nodeB,nodeC])

nodeA.addChild(nodeB)
nodeA.addChild(nodeC)
nodeB.addChild(nodeD)
nodeD.addChild(nodeE)

graph1.addNode(nodeA)
graph1.addNode(nodeB)
graph1.addNode(nodeC)
graph1.addNode(nodeD)
graph1.addNode(nodeE)

print(hasPath(nodeC,nodeE))