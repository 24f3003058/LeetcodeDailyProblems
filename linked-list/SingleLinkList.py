class Node:
    def __init__(self, v=None):

        self.value = v 
        self.next=None

    def is_empty(self):
        if self.value == None:
            return True
        else:
            return False

    def append(self, v):
        if self.is_empty():
            self.value=v
        elif self.next==None:
            self.next =Node(v)
        else:
            self.next.append(v)

        return

    def delete(self,v):
        if self.is_empty():
            return 
        if self.value == v:
            self.value=None
            if self.next != None:
                self.value=self.next.value
                self.next=self.next.next


        else:
            if self.next !=None:
                self.next.delete(v)
                if self.next.value==None:
                    self.next=None
        return

     



