import binaryTree

def createBinarySearchTree(numArray):
    g = binaryTree.Graph()
    root = binaryTree.Node(numArray[0])
    g.addNode(root)

    counter = 1
    currentNode = root
    while(counter < len(numArray)):
        newNode = binaryTree.Node(numArray[counter]) 
        placedNode = False
        while not placedNode:
            if currentNode.value >= numArray[counter]:
                if(currentNode.checkLeftChildEmpty()):
                    currentNode.addChildLeft(newNode)
                    placedNode = True
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if(currentNode.checkRightChildEmpty()):
                    currentNode.addChildRight(newNode)
                    placedNode = True
                else:
                    currentNode = currentNode.getRightChild()                
            
        g.addNode(newNode)
        counter+= 1

    g.displayAdjacencyList()
    return g,root

#numArray = [3,4,2,7,2,10,5]

#createBinarySearchTree(numArray)