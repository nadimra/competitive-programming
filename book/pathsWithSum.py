from randomNode import BinarySearchNode

def pathsWithSum(root,sum):
    r1= 0
    r2 = 0
    r3 = 0
    r1 = pathsWithSumFromRoot(root,sum)
    if root.left:
        r2 = pathsWithSum(root.left,sum)
    if root.right:
        r3 = pathsWithSum(root.right,sum)
    return r1 +r2 + r3

def pathsWithSumFromRoot(treeNode,sum):
    if (sum - treeNode.value) == 0:
        return 1
    elif (sum - treeNode.value) <0:
        return 0
    else:
        if treeNode.left and treeNode.right:
            return pathsWithSumFromRoot(treeNode.left,sum-treeNode.value) + pathsWithSumFromRoot(treeNode.right,sum-treeNode.value)
        elif treeNode.left:
            return pathsWithSumFromRoot(treeNode.left,sum-treeNode.value)
        elif treeNode.right:
            return pathsWithSumFromRoot(treeNode.right,sum-treeNode.value)
        else:
            return 0 

bTree = BinarySearchNode(5)
bTree.append_node(4)
bTree.append_node(2)
bTree.append_node(6)
bTree.append_node(12)
print("--------------")

print(pathsWithSum(bTree,11))
