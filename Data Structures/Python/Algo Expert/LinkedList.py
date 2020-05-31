class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.prev = None
        self.next = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(node)

    def removeNodeWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node. next = None

    def printList(self):
        Node = self.head
        while Node is not None:
            print(f'{Node.value}\t')
            Node = Node.next


if __name__ == "__main__":
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    myList = doublyLinkedList()

    myList.insertAtPosition(1, Node1)
    myList.insertAfter(Node1, Node2)
    print(f'The values after Insetring 1 and 2 :')
    myList.printList()

    myList.remove(Node1)
    print(f'\nThe values after Removing Node 1:')
    myList.printList()

    print(f'\nThe list contains the Node 2:', myList.containsNodeWithValue(2))
    print(f'\nThe list contains the Node 5:', myList.containsNodeWithValue(5))

    