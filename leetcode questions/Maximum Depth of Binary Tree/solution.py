class Solution:
    def maxDepth(self, root):
        return self.recurse(root, 0)

class Node:
    def __init__(self, val, l=None, r=None, height=None):
        self.val = val
        self.l = l
        self.r = r
        self.height = height

nodeN1 = Node(-1)
node0 = Node(0)
node1 = Node(15)
node2 = Node(7)
node3 = Node(18)
node4 = Node(21, node1, node2)
node5 = Node(20, node1, node2)
node6 = Node(9)
node7 = Node(3, node6, node5)

sol = Solution()
print(sol.maxDepth(None))