class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            return IndexError("Stack is empty.")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            return IndexError("Stack is empty.")
    def size(self):
        return len(self)
    def insert(self,index,data):
        return AttributeError("No attribute in 'insert' in stack.")
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top value = ",s1.peek())
print("Size of the stack is ",s1.size())
s1.push(50)
print("Top value = ",s1.peek())
print("Size of the stack is ",s1.size())
