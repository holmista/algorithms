# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

nodeN1 = TreeNode(-1)
node0 = TreeNode(0)
node1 = TreeNode(15)
node2 = TreeNode(0)
node3 = TreeNode(18)
node4 = TreeNode(1)
node5 = TreeNode(0, node4, node2)
node6 = TreeNode(1)
node7 = TreeNode(1, node6, node5)

class Solution:
    def pruneTree(self, root):
        answer = self.recurse(root)
        return answer[1]
    def recurse(self, root):
        if root is None:
            return [True, root]
        leftSubTree = self.recurse(root.left)
        rightSubTree = self.recurse(root.right)
        if leftSubTree[0] == False and root.left.val==0:
            root.left = None
        if rightSubTree[0] == False and root.right.val==0:
            root.right = None
        if root.left is None and root.right is None and root.val == 0:
            return [False]
        return [True, root]


sol = Solution()
root = sol.pruneTree(node7)
print(root.right.right.val)