
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = ListNode()
    current = head
    currentList1 = list1
    currentList2 = list2
    while currentList1 is not None and currentList2 is not None:
        if currentList1.val <= currentList2.val:
            current.next = currentList1
            currentList1 = currentList1.next
            current = current.next
        else:
            current.next = currentList2
            currentList2 = currentList2.next
            current = current.next

    
    if currentList1 is None:
        current.next = currentList2
    else:
        current.next = currentList1
        
    return head.next
    
    
    
def getLinkedList(node):
    values = []
    current = node
    while current is not None:
        values.append(current.val)
        current = current.next
    return values
    

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(3)
n4 = ListNode(4)
n7 = ListNode(7)
n9 = ListNode(9)

n1.next = n4
n4.next = n7

n2.next = n3
n3.next = n9

merged = mergeTwoLists(n1, n2)
print(getLinkedList(merged))