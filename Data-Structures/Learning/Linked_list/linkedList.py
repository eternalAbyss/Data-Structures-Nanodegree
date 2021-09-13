class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = value
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        node