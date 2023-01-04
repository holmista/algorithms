class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        return self.recurse(root, [])
    def recurse(self, node, arr):
        if node is None:
            return
        arr.append(node.val)
        self.recurse(node.left, arr)
        self.recurse(node.right, arr)
        return arr