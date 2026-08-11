class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None

    def is_empty(self):
        return self.front==None

    def enqueue(self,v):
        if self.is_empty():
            self.front=Node(v)
            self.rear=self.front
        else:
            temp=Node(v)
            self.rear.next=temp
            self.rear=temp

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.front.next ==  None:
            temp =self.front.value
            self.front=None
            self.rear=None
        else:
            temp=self.front.value
            self.front=self.front.next

        return temp
               

    def show(self):
        if self.is_empty():
            return None
        else:
            temp=self.front
            while temp != None:
                print(temp.value, end=' ')
                temp=temp.next
            print()

q=Queue()
q.enqueue(10)
q.show()
q.enqueue(20)
q.show()
q.dequeue()
q.show()