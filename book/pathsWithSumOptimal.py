from randomNode import BinarySearchNode


class Solution:
    def pathSum(self,root,sum):
        self.total = 0
        def helper(node,cur):
            
            if node is None:
                return
            
            if node.value + cur == sum:
                self.total += 1

            helper(node.left,cur+node.value)
            helper(node.right,cur+node.value)

            return

        def dfs(node):
            if node is None:
                return
            helper(node,0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(self.total)


bTree = BinarySearchNode(5)
bTree.append_node(4)
bTree.append_node(2)
bTree.append_node(6)
bTree.append_node(12)
print("--------------")

result = Solution()
result.pathSum(bTree,11)