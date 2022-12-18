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
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(5, node4)
node7 = TreeNode(1, node6, node5)
node8 = TreeNode(8, node3, node2)
#           1
#          / \
#         5   2
#        /
#       3

class Solution:
    def findTilt(self, root):
        ans = self.recurse(root, 0, [])
        print(ans[1])
        return sum(ans[1])
    def recurse(self, root, sum, tilts):
        if root is None:
            return [sum, tilts]
        leftVal = 0
        if root.left:
            leftVal = root.left.val
        rightVal = 0
        if root.right:
            rightVal = root.right.val
        left = self.recurse(root.left, sum, tilts)
        right = self.recurse(root.right, sum, tilts)
        left[0]+=leftVal
        right[0]+=rightVal
        tilt = abs(left[0] - right[0])
        tilts.append(tilt)
        return [left[0]+right[0], tilts]

sol = Solution()
print(sol.findTilt(node7))