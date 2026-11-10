class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimums) == 0:
            self.minimums.append(val)
        else:
            self.minimums.append(min(self.minimums[-1], val))

        
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        if len(self.minimums) > 0:
            self.minimums.pop()        

    def top(self) -> int:
        if len(self.stack) > 0:
            t = self.stack[-1] 
            return t     

    def getMin(self) -> int:
        m = self.minimums[-1]
        return m

        
