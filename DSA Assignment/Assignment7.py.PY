class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty.")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty.")
        def size(self):
            return len(self.items)
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element in the stack is ",s1.peek())
print("Removed element is ",s1.pop())
print("Top element in the stack is ",s1.peek())
print()

        