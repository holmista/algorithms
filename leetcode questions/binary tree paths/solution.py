class Solution:
    def binaryTreePaths(self, root):
        paths =  self.recurse(root, [], [])
        converted = []
        for i in paths:
            i = self.convertToStringArrows(i)
            converted.append(i)
        return converted
    def recurse(self, root, path, paths):
        path.append(root.val)
        if root.r is None and root.l is None:
            thePath = [*path]
            paths.append(thePath)
            path.pop()
            print(f'the path: {thePath} path: {path} paths: {paths}')
            return thePath
        print(f'path {path} paths {paths}')
        if(root.l):
            self.recurse(root.l, path, paths)
        if(root.r):
            self.recurse(root.r, path, paths)
        path.pop()
        return paths
    def convertToStringArrows(self, array):
        if isinstance(array, int):return f'{array}'
        if len(array)==0:
            return ''
        res = ''
        for i in array:
            res+=f'->{i}'
        return res[2:]


class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

# node0 = Node(0)
# node1 = Node(5, node0)
# node2 = Node(4)
# node3 = Node(18)
# node4 = Node(21)
# node5 = Node(23, node1, node2)
# node6 = Node(3, node3, node4)
# node7 = Node(7, node5, node6)

node0 = Node(0)
node1 = Node(5)
node2 = Node(4)
node3 = Node(18)
node4 = Node(21)
node5 = Node(23, node1)
node6 = Node(3)
node7 = Node(7, node5, node6)
node7 = Node(7)


sol = Solution()
print(sol.binaryTreePaths(node7))




    
    





    