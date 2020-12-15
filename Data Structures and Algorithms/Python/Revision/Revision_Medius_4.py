from typing import List

'''
Three Sum
'''
# Brute Force

# O(n^3) Time | O(n) Space


def threeSum(array, target):
    result = []
    for firstIdx in range(0, len(array)):
        firstValue = array[firstIdx]
        for secondIdx in range(firstIdx, len(array)):
            secondValue = array[secondIdx]
            for thirdIdx in range(secondIdx, len(array)):
                thirdValue = array[thirdIdx]
                if firstValue + secondValue + thirdValue == target:
                    result.append([firstValue, secondValue, thirdValue])
    return result

# Efficient with sorting
# O(n^2) Time | O(n) Space


def threeSumWithSorting(array, target):
    result = []
    array.sort()
    for idx, each in enumerate(array):
        required = target - each
        startIdx = idx
        endIdx = len(array) - 1
        while startIdx < endIdx:
            first = array[startIdx]
            last = array[endIdx]
            if first + last > required:
                endIdx -= 1
            elif first + last < required:
                startIdx += 1
            else:
                result.append([each, first, last])
                startIdx += 1
                endIdx -= 1

    return result


class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node.value != value

    def remove(self, nodeToRemove):
        node = self.head
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeWithBindings(nodeToRemove)

    def removeNodeWithBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def removeNodeWithvalue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is not None:
            node.pev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is not None:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)


# O(n) Time | O(n) Space
def spiralTraverse(matrix: List[List[int]]) -> List[int]:
    result = []
    startRowIdx, endRowIdx = 0, len(matrix) - 1
    startColIdx, endColIdx = 0, len(matrix[0]) - 1

    while startRowIdx <= endRowIdx and startColIdx <= endColIdx:
        for col in range(startColIdx, endColIdx + 1):
            result.append(matrix[startRowIdx][col])
        for row in range(startRowIdx + 1, endRowIdx + 1):
            result.append(matrix[row][endColIdx])
        for col in reversed(range(startColIdx, endColIdx)):
            if startRowIdx == endRowIdx:
                break
            result.append(matrix[endRowIdx][col])
        for row in reversed(range(startRowIdx + 1, endRowIdx)):
            if startColIdx == endColIdx:
                break
            result.append(matrix[row][startColIdx])
        startRowIdx += 1
        endRowIdx -= 1
        startColIdx += 1
        endColIdx -= 1
    return result


# O(n) Time | O(1) Space
def longestPeak(array):
    peaks = getAllPeaks(array)
    longest = float('-inf')
    for peak in peaks:
        longest = max(longest, getPeakSize(peak, array))
    return longest if longest != float('-inf') else 0


def getPeakSize(peak, arr):
    start = end = peak
    while start >= 0 and arr[start - 1] < arr[start]:
        start -= 1
    while end < len(arr) and arr[end] > arr[end + 1]:
        end += 1

    return end - start + 1


def getAllPeaks(arr):
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append(i)
    return peaks


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        return self

    def contains(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False

    def remove(self, value, parent=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.right:
                parent = curr
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.getMinValue()
                    curr.right.remove(curr.value, curr)
                elif parent is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        curr = None
                elif parent.left == curr:
                    curr.left = curr.left if curr.left is not None else curr.right
                elif parent.right == curr:
                    curr.right = curr.left if curr.left is not None else curr.right
                break
            return

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value


if __name__ == "__main__":
    # array = [12, 3, 1, 2, -6, 5, -8, 6, 7]
    # target = 0
    # print(threeSum(array, target))
    # print(threeSumWithSorting(array, target))
    # matrix = [
    #     [1, 2, 3, 4],
    #     [12, 13, 14, 5],
    #     [11, 16, 15, 6],
    #     [10, 9, 8, 7]]
    # print(spiralTraverse(matrix))

    arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(arr))
