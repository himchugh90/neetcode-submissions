class MyStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        # if self.stack:
        self.stack.append(x)
        # else:

        

    def pop(self) -> int:
        if self.stack:
            # return self.stack.remove(self.stack[-1])
            return self.stack.pop()
            # return stack[-1]
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

        

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()