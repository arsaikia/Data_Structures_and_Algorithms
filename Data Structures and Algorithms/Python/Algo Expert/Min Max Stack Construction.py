# Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self):
        self.stack = []
    
    def getCurr(self):
        currVal = self.stack[-1] if len(self.stack)>0 else []
        return currVal

    def peek(self):
        currVal = self.getCurr()
        return currVal[0]

    def pop(self):
        poppedVal = self.stack.pop()
        return poppedVal[0]

    def push(self, number):
        currVal = self.getCurr()
        currMin = currVal[1] if len(currVal) > 0 else number
        currMax = currVal[2] if len(currVal) > 0 else number
        self.stack.append([number, min(currMin, number), max(currMax, number)])

    def getMin(self):
        return self.getCurr()[1]

    def getMax(self):
        return self.getCurr()[2]


if __name__ == "__main__":
    stack = MinMaxStack()
    
    stack.push(5)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    
    stack.push(7)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    
    stack.push(2)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    
    print(stack.pop())
    print(stack.pop())
    
    print(stack.getMin())
    print(stack.getMax())
    
    print(stack.peek())
    
    
    