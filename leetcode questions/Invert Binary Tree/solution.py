class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

nodeN1 = TreeNode(-1)
node0 = TreeNode(0)
node1 = TreeNode(15)
node2 = TreeNode(7, None, node1)
node3 = TreeNode(18)
node4 = TreeNode(21, node1)
node5 = TreeNode(20, node4, node2)
node6 = TreeNode(9)
node7 = TreeNode(3, node6, node5)

class Solution:
    def invertTree(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
sol = Solution()
print(sol.invertTree(node7).left.val)