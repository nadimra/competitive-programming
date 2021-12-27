import graph

def nodesThatDependOn(g,node):
    nodes = []
    for nodeCheck in g.nodes:
        if node in nodeCheck.children:
            nodes.append(nodeCheck)
    return nodes

def buildOrder(g):
    dependancyMap = {}
    order = []
    for node in g.nodes:
        dependancies = nodesThatDependOn(g,node)
        dependancyMap[node] = len(dependancies)
    
    for key in dependancyMap:
        print(key.name)
        print(dependancyMap[key])

    
    while not all(v == 0 for v in dependancyMap.values()):
        if 0 not in dependancyMap.values():
            return None
        else:
            for key in dependancyMap:
                if dependancyMap[key]==0 and key not in order:
                    print("Added "+str(key.name))
                    order.append(key)
                    break
            
            for node in order[-1].children:
                #print(node.name)
                dependancyMap[node] = dependancyMap[node]-1

    for key in dependancyMap:
        if key not in order:
            order.append(key)
            print("Added "+str(key.name))

    return order
    

graph1 = graph.Graph()
nodeG = graph.Node("G")
nodeF = graph.Node("F")
nodeE = graph.Node("E")
nodeD = graph.Node("D")
nodeC = graph.Node("C")
nodeB = graph.Node("B")
nodeA = graph.Node("A")

nodeA.addChild(nodeE)
nodeB.addChild(nodeA)
nodeB.addChild(nodeE)
nodeC.addChild(nodeA)
nodeD.addChild(nodeG)
nodeF.addChild(nodeC)
nodeF.addChild(nodeA)
nodeF.addChild(nodeB)

graph1.addNode(nodeA)
graph1.addNode(nodeB)
graph1.addNode(nodeC)
graph1.addNode(nodeD)
graph1.addNode(nodeE)
graph1.addNode(nodeF)
graph1.addNode(nodeG)

buildOrder(graph1)