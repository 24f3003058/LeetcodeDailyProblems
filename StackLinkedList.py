class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None

class Stack:
    def __init__(self):
        self.top=None


    def is_Empty(self):
        if self.top==None:
            return True

    def push(self,v):
        if self.is_Empty():
            self.top=Node(v)
        else:
            temp=Node(v)
            temp.next=self.top
            self.top=temp 

    def pop(self):
        if self.is_Empty():
            return None
        else:
            temp_value=self.top.value
            self.top=self.top.next
            return temp_value
    def show(self):
        if self.is_Empty():
            return None
        else:
            temp=self.top
            while temp != None:
                print(temp.value)
                temp=temp.next    

s=Stack()
s.show()
s.push(10)
s.show()
s.push(100)
s.show()
s.pop()
s.show()    