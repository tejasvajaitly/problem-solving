class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        size = len(self.q)
        self.q.appendleft(x)
        while size:
            tmp = self.q.pop()
            self.q.appendleft(tmp)
            size -= 1

    def pop(self) -> int:
        if not self.empty():
            res = self.q.pop()
            return res
        else:
            None

    def top(self) -> int:
        if not self.empty():
            return self.q[-1]
        else:
            None

    def empty(self) -> bool:
        return False if len(self.q) > 0 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()