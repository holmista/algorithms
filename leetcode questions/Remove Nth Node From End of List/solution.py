# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        self.recurse(dummy, n)
        return dummy.next
    def recurse(self, node, n):
        if node is None:
            return 0
        idx = self.recurse(node.next, n) + 1
        # print(idx, node.val)
        if idx == n+1:
            print(f'found: {idx, node.val}')
            lastPart = None
            if node.next is not None:
                lastPart = node.next.next
            node.next.next = None
            node.next = lastPart
        return idx

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

def printLinkedList(head):
    while head is not None:
        print(head.val)
        head = head.next
    return

sol = Solution()
answer = sol.removeNthFromEnd(n4, 1)
printLinkedList(answer)
