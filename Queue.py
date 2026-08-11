class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return self.queue==[]
    
    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        val= None
        if not self.is_empty():
           val=self.queue[0]
           self.queue =self.queue[1:]
        return val

    def __str__(self):
        return (str(self.queue))

q=Queue()
print(q)
q.enqueue(10)
print(q)
q.enqueue(20)
print(q)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
print(q)
print(q.dequeue())
print(q)


