class MinStack:

    def __init__(self):
        self.values = []
        self.min = float("inf")
        self.mins = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if val <= self.min: 
            self.min = val
            self.mins.append(val)

    def pop(self) -> None:
        val = self.values.pop()
        if val == self.min:
            self.mins.pop()
            if len(self.mins)>0:
                self.min=self.mins[-1]
            else:
                self.min = float("inf")
            
    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
# obj.push(1)
# obj.push(0)
# obj.getMin()
print(obj.mins)
obj.pop()
obj.getMin()
print(obj.mins)
obj.pop()
obj.getMin()
print(obj.mins)
obj.pop()
print(obj.mins)
obj.push(2147483647)
print 
obj.getMin()
# param_3 = obj.top()
# param_4 = obj.getMin()