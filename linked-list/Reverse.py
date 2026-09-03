# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k==0:
            return head
         
        # find len and tail of linked list
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        
        k=k%n
        if k==0:
            return head
        
        tail.next=head

        #new tail
        steps_to_new_tail=n-k-1
        new_tail=head
        for i in range(steps_to_new_tail):
            new_tail=new_tail.next

        new_head=new_tail.next
        new_tail.next=None
        return new_head

