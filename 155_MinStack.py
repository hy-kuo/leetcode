import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []
        self.index = 0

    def push(self, x: 'int') -> 'None':
        self.stack.append(x)
        if self.index == 0:
            self.min = [x]
        else:
            self.min.append(min(self.min[self.index-1], x))
        self.index +=1

    def pop(self) -> 'None':
        del self.stack[self.index-1] 
        del self.min[self.index-1] 
        self.index -=1

    def top(self) -> 'int':
        return self.stack[self.index-1]

    def getMin(self) -> 'int':
        return self.min[self.index-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()