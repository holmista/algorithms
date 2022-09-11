class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head is None or head.next is None or head.next.next is None:
        return False
    pointer1 = head.next
    pointer2 = head.next.next
    while True:
        if pointer1 is None or pointer2 is None:
            return False
        if pointer1 is pointer2:
            return True
        try:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        except:
            return False
    


    