class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SolutionBrute:
    def diameterOfBinaryTree(self, root):
        res = self.recurseDiameter(root,[])
        return max(res)
    def longestPath(self,node):
        if node is None:
            return 0
        leftPathLen = self.longestPath(node.left)+1
        rightPathLen = self.longestPath(node.right)+1
        return max(leftPathLen, rightPathLen)
    def recurseDiameter(self, node, arr):
        if node is None:
            arr.append(0)
            return
        maxLeftLen =  self.longestPath(node.left)
        maxRightLen =  self.longestPath(node.right)
        arr.append(maxLeftLen+maxRightLen)
        self.recurseDiameter(node.left,arr)
        self.recurseDiameter(node.right,arr)
        return arr

# I was not able to improve brute force solution cuz I underetimated the power of global variables, they can be very useful in recursion.
# In the above example I also was trying to utilize max but I was doing it by passing max to a recursive function but max has to be calculated after
# I get results recursively, so it was not working at all but maxx variable fixed it. I don't need to pass maxx value to a recursive function. It simply
# modifies the maxx value and in the end I return it.
class Solution:
    def __init__(self):
        self.maxx = 0
    def diameterOfBinaryTree(self, root):
        self.dsf(root)
        return self.maxx
    def dsf(self, node):
        if node is None:
            return 0
        left = self.dsf(node.left)
        right = self.dsf(node.right)
        print(left+right, self.maxx, node.val)
        self.maxx = max(self.maxx, left+right)
        return 1+max(left, right)

        
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6

sol = Solution()
print(sol.diameterOfBinaryTree(node1))