class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def mergeSortedList(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    
    if head1.data <= head2.data:
        mergedHead=head1
        current1=head1.next
        current2=head2
    else:
        mergedHead=head2
        current1=head1
        current2=head2.next
    tail=mergedHead  
        
    while current1 is not None and current2 is not None:
        if current1.data <= current2.data:
            tail.next=current1
            current1=current1.next
        else: 
            tail.next=current2
            current2=current2.next
        tail=tail.next
    tail.next=current1  if current1 is not None else current2
    return mergedHead