class MinStack:

    def __init__(self):
        self.stk=[]

    def push(self, value: int) -> None:
        if not self.stk:
            self.stk.append([value,value])
        else:
            mini=min(value,self.stk[-1][1])
            self.stk.append([value,mini])
        

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()


    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]
        

    def getMin(self) -> int:
        return self.stk[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()