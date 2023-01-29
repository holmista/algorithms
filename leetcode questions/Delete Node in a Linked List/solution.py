class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        curr = node
        next = curr.next
        while next.next is not None:
            curr.val, next.val = next.val, curr.val
            curr = next
            next = curr.next
        curr.val, next.val = next.val, curr.val
        curr.next = None
        
def printList(node):
    if node is None:
        return 
    print(node.val)
    printList(node.next)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4

sol = Solution()
sol.deleteNode(l3)
printList(l1)
