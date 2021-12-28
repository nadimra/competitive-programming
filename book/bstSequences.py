import bst
import itertools
import binaryTree

depthMap = {}

def listOfDepths(depthLevel,root):
    if root.children == [None,None]:
        return
    else:
        for child in root.children:
            if child is not None:
                siblingsList = depthMap.get(depthLevel,[])
                siblingsList.append(child.value)
                depthMap[depthLevel] = siblingsList
                listOfDepths(depthLevel+1,child)

def mergeLists(depthLevel,currentAccumulation):
    siblings = depthMap[depthLevel]
    permutations = list(itertools.permutations(siblings))
    newAccumulation = []
    for permutation in permutations:
        permutation = list(permutation)
        for currentAccum in currentAccumulation:
            newAccum = permutation + currentAccum
            newAccumulation.append(newAccum)
        if(len(currentAccumulation)==0):
            newAccumulation.append(permutation)
    if(depthLevel == 0):
        print(newAccumulation)
    else:
        mergeLists(depthLevel-1,newAccumulation)

def bstSequences(g,root):
    depthMap[0] = [root.value]
    listOfDepths(1,root)
    mergeLists(max(depthMap, key = int),[])

#numArray = [3,4,2,7,2,10,5]
#g,root = bst.createBinarySearchTree(numArray)
g = binaryTree.Graph()

nodeC = binaryTree.Node(3)
nodeB = binaryTree.Node(1)
nodeA = binaryTree.Node(2)
nodeA.addChildLeft(nodeB)
nodeA.addChildRight(nodeC)

g.addNode(nodeA)
g.addNode(nodeB)
g.addNode(nodeC)

bstSequences(g,nodeA)


