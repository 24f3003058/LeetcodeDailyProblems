class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def removeDuplicate(head):
    if head is None:
        return
    c = head
    while c is not None and c.next is not None:
        if c.value == c.next.value:
            c.next = c.next.next
        else:
            c = c.next

