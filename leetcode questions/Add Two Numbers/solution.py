class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0
        summ = 0
        while l1 or l2:
            if not l1:
                summ = l2.val + carry
            if not l2:
                summ = l1.val + carry
            if l1 and l2:
                summ = l1.val + l2.val + carry
            if summ > 9:
                curr.next = ListNode(summ%10)
                carry = 1
            else:
                curr.next = ListNode(summ)
                carry = 0
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            curr.next = ListNode(1)
        return dummy.next