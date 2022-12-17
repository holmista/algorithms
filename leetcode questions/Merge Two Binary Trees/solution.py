class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

nodeN1 = TreeNode(-1)
node0 = TreeNode(0)
node1 = TreeNode(15)
node2 = TreeNode(0, None, node0)
node3 = TreeNode(18, None, node1)
node4 = TreeNode(1)
node5 = TreeNode(0)
node6 = TreeNode(1, node4)
node7 = TreeNode(1, node6, node5)
node8 = TreeNode(8, node3, node2)
# 7, 8, 6, 3, 5, 2
class Solution:
    def mergeTrees(self, root1, root2):
        return self.recurse(root1, root2, TreeNode())
    def recurse(self, root1, root2, root3):
        if root1 is None and root2 is None:
            return None
        if root1 and root2:
            root3.val = root1.val + root2.val
            root3.left = self.recurse(root1.left, root2.left, TreeNode())
            root3.right = self.recurse(root1.right, root2.right, TreeNode())
        elif root2:
            root3 = root2
        elif root1:
            root3 = root1
        return root3


sol = Solution()    
res = sol.recurse(node8, node7, TreeNode())

def printBinaryTree(node):
    if node is None:
        return
    print(node.val)
    printBinaryTree(node.left)
    printBinaryTree(node.right)

printBinaryTree(res)