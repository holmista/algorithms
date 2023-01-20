class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p is bigger than root and q is bigger than root, root = root.right
        # if p is less than root and q is less than root, root = root.left
        # else return root
         while True:
            if p.val>root.val and q.val>root.val:
                root = root.right
            elif p.val<root.val and q.val<root.val:
                root = root.left
            else:
                return root
            
# [3,1,4,null,2]
t1 = TreeNode(3)
t2 = TreeNode(1)
t3 = TreeNode(4)
t4 = TreeNode(2)
t1.left = t2
t1.right = t3
t2.right = t4

sol = Solution()
sol.lowestCommonAncestor(t1, t4, t3)