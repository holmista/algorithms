class Solution:
    def isBalanced(self, root):
       return self.recurse(root)[0]
    def recurse(self, root):
        if not root:
            return [True, 0]
        left = self.recurse(root.l)
        right = self.recurse(root.r)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, max( left[1], right[1] ) + 1]

class Node:
    def __init__(self, val, l=None, r=None, height=None):
        self.val = val
        self.l = l
        self.r = r
        self.height = height

nodeN1 = Node(-1)
node0 = Node(0)
node1 = Node(5, node0)
node2 = Node(4)
node3 = Node(18)
node4 = Node(21, node1, node2)
node5 = Node(23, node1, node2)
node6 = Node(3)
node7 = Node(7, node6, node5)
  
sol = Solution()
print(sol.isBalanced(node0))















