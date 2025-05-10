class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        return self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue underflow.")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue underflow.")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue underflow.")
    def size(self):
        return len(self.items)
q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print("Size of Queue is ",q1.size(),".")
print("Front= ",q1.get_front(),"Rear= ",q1.get_rear())
try:
    q1.dequeue()
    print("Size of Queue is ",q1.size(),".")
except IndexError as e:
    print(e.args[0])
        
        