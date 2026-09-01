class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.head=None
        self.last=None

    def insert_end(self,data):
        newnode=Node(data)
        newnode.prev=self.last
        if self.head == None:
            self.head=newnode
            self.last=newnode
        else:
            self.last.next=newnode
            self.last=newnode

    def insert_at_pos(self,data,pos):
        newnode=Node(data)
        current=self.head
        count=1
        while current is not None and count<pos:
            current=self.head
            count+=1

        if current is None :
            return 
        prev_node=current.prev
        newnode.next=current
        newnode.prev=prev_node
        prev_node.next=newnode
        current.prev=newnode
        
