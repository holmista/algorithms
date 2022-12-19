class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node0 = TreeNode(10)
node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(6, node0, node2)
node4 = TreeNode(21, node1, node2)
node5 = TreeNode(20)
node6 = TreeNode(8, node2, node0)
node7 = TreeNode(9, node6, node5)

#       9
#      / \
#     8  20
#    / \
#   7  10



class Solution:
    def isValidBST(self, root):
        return self.recurse(root, float('-inf'), float('inf'))
    def recurse(self, node, left, right):
        if node is None:
            return True
        if node.val < right and node.val>left:
            leftValid = self.recurse(node.left, left, node.val)
            rightValid = self.recurse(node.right, node.val, right)
            return leftValid and rightValid
        else:
            return False
        

sol = Solution()
print(sol.isValidBST(node7))
        
        