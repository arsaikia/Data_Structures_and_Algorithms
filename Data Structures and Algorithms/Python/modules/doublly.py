class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def remove(self, nodeToRemove):
        node = self.head
        if nodeToRemove is self.head:
            self.head = self.head.next
        elif nodeToRemove is self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(nodeToRemove)

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def removeNodeWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if self.tail is nodeToInsert:
            return
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, nodeToInsert, position):
        currPosition = 1
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        while node is not None and currPosition < position:
            currPosition += 1
            node = node.next
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def setHead(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.head is None and self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def printList(self):
        node = self.head
        while node is not None:
            print("--->", node.value, end=" <---")
            node = node.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    first = Node(10)
    dll.setHead(first)
    dll.setTail(Node(20))
    dll.insertAtPosition(Node(15), 3)
    newFirst = Node(5)
    dll.insertBefore(first, newFirst)
    dll.remove(newFirst)

    dll.printList()
