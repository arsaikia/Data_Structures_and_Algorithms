'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myStack = []
        

    def push(self, x: int) -> None:
        
        self.myStack.append(x)
        

    def pop(self) -> None:
        
         self.myStack.pop()

    def top(self) -> int:
         return self.myStack[len(self.myStack)-1]

    def getMin(self) -> int:
        return min(self.myStack)
        




if __name__ == "__main__":
    
    #Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    print(obj.myStack)