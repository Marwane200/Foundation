class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        if not self.stack: self.stack.append((val, val))
        else:
            if val < self.stack[-1][1]: self.stack.append((val,val))
            else: self.stack.append((val,self.stack[-1][1]))

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


#Test Cases
Stack = MinStack()
Stack.push(8)
Stack.push(-1)
Stack.push(9)
Stack.push(6)
print(Stack.getMin())
print(Stack.top())
Stack.pop
