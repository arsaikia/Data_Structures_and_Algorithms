# ----------------------------------------< Doubly Linked List >-----------------------------------------------

# Define a Node class
class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

# Define a Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNode(self, nodeToRemove):
        # Check if the node to remove is the head of dll
        if self.head is nodeToRemove:
            self.head = self.head.next
        # Check if the node to remove is the tail of dll
        if self.tail is nodeToRemove:
            self.tail = self.tail.prev
        # Remove remaining bindings if head/tail, else all bindings
        self.removeBindings(nodeToRemove)

    def removeBindings(self, nodeToRemove):
        # Check if we have a previous node
        # If we just removed a head, previous will be None
        if nodeToRemove.prev is not None:
            nodeToRemove.prev.next = nodeToRemove.next
        # Check if we have a next node
        # If we just removed a tail, next will be None
        if nodeToRemove.next is not None:
            nodeToRemove.next.prev = nodeToRemove.prev
        nodeToRemove.next = None
        nodeToRemove.prev = None

    def removeNodeWithValue(self, value):
        # Traverse from head
        node = self.head
        while node is not None:
            # For every node check if the value is same
            # as what we want to remove and if yes the remove
            # There might b multiple nodes we need to remove
            # Which is why we traverse the whole list -> O(n) Time
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.removeNode(nodeToRemove)

    def insertBefore(self, node, nodeToInsert):
        # If we have only head and tail, remove and add == do nothing
        if self.head is nodeToInsert and self.tail is nodeToInsert:
            return
        self.removeNode(nodeToInsert)
        # At least two nodes
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        # If the `node` is head
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # If we have only head and tail, remove and add == do nothing
        if self.head is nodeToInsert and self.tail is nodeToInsert:
            return
        self.removeNode(nodeToInsert)
        # At least two nodes
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        # If the `node` is tail
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Remove the node if it is already there
        self.removeNode(nodeToInsert)
        # Position 1 means we need to set the head of the list
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            position += 1
        # We exit the loop when either:
        # 1. Reached the end of list
        # 2. position is correct
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


# ----------------------------------------< Doubly Linked List >-----------------------------------------------

# O(n^2) Time | O(n) Space
def threeSum(array, target):
    array.sort()
    for idx, num in enumerate(array):
        required = target - num
        leftIdx = idx + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            if array[leftIdx] + array[rightIdx] == required:
                return True
            elif array[leftIdx] + array[rightIdx] > required:
                rightIdx -= 1
            else:
                leftIdx += 1
    return False


if __name__ == "__main__":
    print(threeSum([2, 4, 6, 8, 12, 14, 16, 20, 22], 22))
