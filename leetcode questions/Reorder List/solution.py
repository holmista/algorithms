class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        if head.next is None or head.next.next is None:
            return head
        curr = head
        secondLast = self.getSecondLastNode(head)
        while curr:
            if curr.next is None:
                break
            # secondLast = self.getSecondLastNode(head)
            lastNode = secondLast.next
            secondLast.next = None
            self.insertNode(curr,lastNode)
            curr = lastNode.next
        return head
    def getSecondLastNode(self, node):
        if node is None or node.next is None:
            return None
        if node.next.next is None:
            return node
        return self.getSecondLastNode(node.next)
    def insertNode(self, head, node):
        prev = head.next
        head.next = node
        node.next = prev
    def printList(self, node):
        if node is None: 
            return
        print(node.val)
        self.printList(node.next)

class Solution2:
    def reorderList(self, head) -> None:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        l = 0
        r = len(arr)-1
        while l<r-1:
            arr[l].next = arr[r]
            arr[r].next = arr[l+1]
            arr[r-1].next = None
            l+=1
            r-=1
            # self.printList(head)
        return head
    def printList(self, node):
        if node is None: 
            return
        print(node.val)
        self.printList(node.next)


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

sol = Solution2()
res = sol.reorderList(n1)
sol.printList(res)


# 1->2->3->4->5
# 1->5->2->3->4
# 1->5->2->4->3
