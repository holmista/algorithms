class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        iterCount = self.listLength(head)//k
        idx = 0
        end = head
        start = head
        dummy = ListNode()
        curr = dummy
        for _ in range(iterCount):
            while idx+1<k:
                end = end.next
                idx+=1
            idx=0
            next = end.next
            end.next = None
            reversed = self.reverseList(start)
            curr.next = reversed
            curr = start
            end,start = next,next
        if next:
            curr.next = next
        return dummy.next
    def listLength(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
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

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

sol = Solution()
res = sol.reverseKGroup(n1,2)
sol.printList(res)


