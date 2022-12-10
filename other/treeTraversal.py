class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

node1 = Node(5)
node2 = Node(4)
node3 = Node(18)
node4 = Node(21)
node5 = Node(23, node1, node2)
node6 = Node(3, node3, node4)
node7 = Node(7, node5, node6)

def preOrderTraverse(node, path):
    if node == None: return path
    path.append(node.val)
    preOrderTraverse(node.l, path)
    preOrderTraverse(node.r, path)
    return path

print(preOrderTraverse(node7, []))

def inOrderTraverse(node, path):
    if node == None: return path
    inOrderTraverse(node.l, path)
    path.append(node.val)
    inOrderTraverse(node.r, path)
    return path

print(inOrderTraverse(node7, []))

def postOrderTraverse(node, path):
    if node == None: return path
    postOrderTraverse(node.l, path)
    postOrderTraverse(node.r, path)
    path.append(node.val)
    return path

def breadthFirstSearch(root):
    queue = [root]
    path = []
    while len(queue)>0:
        curr = queue[0]
        if curr.l:
            queue.append(curr.l)
        if curr.r:
            queue.append(curr.r)
        path.append(queue.pop(0).val)
    return path
        

print(breadthFirstSearch(node7))
