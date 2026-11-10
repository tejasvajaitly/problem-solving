class Node:
    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node('')
        self.tail = Node('')
        self.curr = Node(homepage)
        self.head.next = self.curr
        self.curr.prev = self.head
        self.curr.next = self.tail
        self.tail.prev = self.curr

    def visit(self, url: str) -> None:
        newNode = Node(url)
        a = self.curr
        b = self.tail

        a.next = newNode
        newNode.prev = a

        newNode.next = b
        b.prev = newNode

        self.curr = newNode

    def back(self, steps: int) -> str:
        while steps and self.curr.prev != self.head:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps and self.curr.next != self.tail:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val        
   
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)