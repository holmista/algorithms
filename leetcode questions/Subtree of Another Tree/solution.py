# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root, subRoot):
        return self.dfs(root, subRoot)
    def dfs(self,root, subRoot):
        if not subRoot: return True
        if not root: return False
        if self.compare(root,subRoot):
            return True
        if self.dfs(root.left,subRoot) or self.dfs(root.right,subRoot):
            return True
        return False
    def compare(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val==node2.val:   
            leftSame = self.compare(node1.left, node2.left)
            rightSame = self.compare(node1.right, node2.right)
            return leftSame and rightSame
        return False
    
        
                

node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

#       4               4
#      | \             |  \
#      0  1            0   none
#
node3.left = node4
node2.right = node5

node4.left = node1
node4.right = node2

subroot = TreeNode(2)
# subroot.left = TreeNode(1)
# subroot.right = TreeNode(2)
# node5.right = TreeNode(2)

sol = Solution()
print(sol.isSubtree(node2, node5))


