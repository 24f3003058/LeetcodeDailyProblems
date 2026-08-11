class Stack:
    def __init__(self):
        self.stack=[]

    def  is_empty(self):
        return (self.stack==[])

    def push(self,v):
        self.stack.append(v)

    def pop(self):
        v=None
        if not self.is_empty() :
            v=self.stack.pop()   
        return v
    def __str__(self):
        return (str(self.stack))
s=Stack()
print(s)
s.push(10)
print(s)

s.push(9)
print(s)
s.push(13)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
print(s.pop())
