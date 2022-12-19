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
node6 = TreeNode(9)
node7 = TreeNode(9)

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False

sol = Solution()
print(sol.isSameTree(node6, node7))