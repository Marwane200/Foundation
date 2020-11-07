'''
STACKS & QUEUES

Stacks and Queues are another fundamental data structure.
This class shows unique implmentations of this.
'''
class MinStack:
    '''
    MIN STACK:
    minStack that is designed to support push, pop, top
    but also retrievs the minimum element in constant time.
    '''
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
        print(self.stack[-1][0])
        return self.stack[-1][0]

    def getMin(self):
        print(self.stack[-1][1])
        return self.stack[-1][1]


#Test Cases
minStack = MinStack()

#Using Min stack
minStack.push(8)
minStack.push(-1)
minStack.push(9)
minStack.push(6)
minStack.getMin()
minStack.top()
minStack.pop
