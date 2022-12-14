class Solution:
    def minDepth(self, root):
        return self.recurse(root)
    def recurse(self, root):
        if root is None:
            return 0
        leftDepth = self.recurse(root.l)
        rightDepth = self.recurse(root.r)
        print(root.val, leftDepth, rightDepth, min(leftDepth, rightDepth) + 1)
        if leftDepth == 0: return rightDepth + 1
        if rightDepth == 0: return leftDepth + 1
        return min(leftDepth, rightDepth) + 1

class Node:
    def __init__(self, val, l=None, r=None, height=None):
        self.val = val
        self.l = l
        self.r = r
        self.height = height

nodeN1 = Node(-1)
node0 = Node(0)
node1 = Node(15)
node2 = Node(7, None, node1)
node3 = Node(18)
node4 = Node(21, node1)
node5 = Node(20, None, node2)
node6 = Node(9)
node7 = Node(3, None, node5)

sol = Solution()
print(sol.minDepth(node7))