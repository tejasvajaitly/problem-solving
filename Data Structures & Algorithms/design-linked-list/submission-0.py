class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            node = self.findNode(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        a = self.head
        b = self.head.next
        self.insert(newNode, a, b)

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        a = self.tail.prev
        b = self.tail
        self.insert(newNode, a, b)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        else:
            newNode = Node(val)
            indexThNode = self.findNode(index)
            a = indexThNode.prev
            b = indexThNode
            self.insert(newNode, a, b)


    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            indexThNode = self.findNode(index)
            a = indexThNode.prev
            b = indexThNode.next

            a.next = b
            b.prev = a

            self.size -= 1
    

    def findNode(self, index: int) -> Node:
        pointer = self.head.next
        while index:
            pointer = pointer.next
            index -= 1
        return pointer
    
    def insert(self, newNode: Node, a: Node, b: Node) -> None:
        a.next = newNode
        newNode.prev = a

        newNode.next = b
        b.prev = newNode

        self.size += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)