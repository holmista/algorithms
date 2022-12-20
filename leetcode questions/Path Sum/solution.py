class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node0 = TreeNode(10)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7, node6, node5)

class Solution:
    def hasPathSum(self, root, targetSum):
        return self.recurse(root, targetSum, 0)
    def recurse(self, node, targetSum, currentSum):
        if not node:
            return False
        currentSum+=node.val
        print(currentSum)
        if not node.left and not node.right:
            return currentSum == targetSum
        return (self.recurse(node.left, targetSum, currentSum) or self.recurse(node.right, targetSum, currentSum))
    def findLeaves(self, node, arr=[]):
        if node.left is None and node.right is None:
            arr.append(node)
        if node.left:
            self.findLeaves(node.left, arr)
        if node.right:
            self.findLeaves(node.right, arr)
        return arr

sol = Solution()
print(sol.hasPathSum(node7, 13))        

