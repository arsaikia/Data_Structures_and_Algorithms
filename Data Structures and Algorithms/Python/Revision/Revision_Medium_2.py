# O(n^2) Time | O(n) Space
from ast import NodeTransformer


def threeSum(array, target):
    array.sort()
    output = []

    for idx, num in enumerate(array):
        required = target - num
        start, end = idx + 1, len(array) - 1
        while start < end:
            firstElement = array[start]
            secondElement = array[end]
            if firstElement + secondElement == required:
                output.append([num, firstElement, secondElement])
                start += 1
                end -= 1
            elif firstElement + secondElement < required:
                start += 1
            elif firstElement + secondElement > required:
                end -= 1
    return output


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value) -> bool:
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def remove(self, nodeToRemove):
        if nodeToRemove == self.head:
            self.head = self.head.next
        if nodeToRemove == self.tail:
            self.tail = self.tail.prev
        self.removeNodeWithBindings(nodeToRemove)

    def removeNodeWithBindings(self, nodeToRemove):
        if nodeToRemove.prev is not None:
            nodeToRemove.prev.next = nodeToRemove.next
        if nodeToRemove.next is not None:
            nodeToRemove.next.prev = nodeToRemove.prev
        nodeToRemove.prev = None
        nodeToRemove.next = None

    def removeNodeWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def insertBefore(self, node, nodeToInsert):
        if self.head == nodeToInsert and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is not None:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
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
        currPosition = 1
        while node is not None and currPosition != position:
            currPosition += 1
            node = node.next
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

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

    def printList(self):
        node = self.head
        result = []
        while node is not None:
            result.append(node.value)
            node = node.next
        print(result)


if __name__ == "__main__":
    # arr = [12, 3, 1, 2, -6, 5, -8, 6]
    # targetSum = 0
    # print(threeSum(arr, targetSum))

    # Doubly Linked List
    ll = DoublyLinkedList()
    ll.setHead(Node(1))
    node = Node(3)
    ll.insertAfter(ll.head, node)
    ll.insertBefore(ll.tail, Node(2))

    ll.insertAtPosition(4, Node(4))
    ll.setHead(Node(-100))
    ll.setTail(Node(100))

    ll.removeNodeWithValue(4)
    ll.remove(node)

    ll.tail = ll.head

    ll.printList()
