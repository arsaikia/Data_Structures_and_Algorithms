# O(n^2) Time | O(n) Space
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

    # O(n) Time | O(1) Space
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


# O(nm) Time where n = row and m = col in matrix; O(mn) Space
# We mst traverse all elements once and store the elements in an Auxiliary array
def spiralTraverse(array):
    rowStart, rowEnd = 0, len(array) - 1
    colStart, colEnd = 0, len(array[0]) - 1
    result = []

    while rowStart < rowEnd and colStart < colEnd:
        for col in range(colStart, colEnd + 1):
            result.append(array[rowStart][col])
        for row in range(rowStart + 1, rowEnd + 1):
            result.append(array[row][colEnd])
        for col in reversed(range(colStart, colEnd)):
            if rowStart == rowEnd:
                continue
            result.append(array[rowEnd][col])
        for row in reversed(range(rowStart + 1, rowEnd)):
            if colStart == colEnd:
                continue
            result.append(array[row][colStart])

        rowStart += 1
        rowEnd -= 1
        colStart += 1
        colEnd -= 1

    return result


def longestPeak(array):
    if len(array) < 3:
        return 0
    peaks = getPeaks(array)
    globalMax = 0
    for peak in peaks:
        currMax = 0
        start = peak
        while start - 1 >= 0 and array[start - 1] < array[start]:
            start -= 1

        end = peak
        while end + 1 <= len(array) - 1 and array[end + 1] < array[end]:
            end += 1

        currMax = end - start + 1
        globalMax = max(currMax, globalMax)

    return globalMax


def getPeaks(arr):
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            peaks.append(i)
    return peaks


def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    arrOneIdx, arrTwoIdx = 0, 0
    smallestGlobal = float("inf")
    smallest = []

    while arrOneIdx < len(arr1) and arrTwoIdx < len(arr2):
        numberOne = arr1[arrOneIdx]
        numberTwo = arr2[arrTwoIdx]
        if numberOne > numberTwo:
            arrTwoIdx += 1
        elif numberTwo > numberOne:
            arrOneIdx += 1
        else:
            return [numberOne, numberTwo]

        if abs(numberOne - numberTwo) < smallestGlobal:
            smallestGlobal = abs(numberOne - numberTwo)
            smallest = [numberOne, numberTwo]
    return smallest


# O(n) Time | O(1) Space
def moveElementsToEnd(array, toMove):
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] == toMove and array[end] != toMove:
            swap(array, start, end)

        elif array[start] != toMove:
            start += 1
        elif array[end] == toMove:
            end -= 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def isMonotnicArray(array):
    increasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing = False

    decreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
    return increasing or decreasing


class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right
        return self

    def printBst(self):
        node = self
        if node.left is not None:
            node.left.printBst()

        print(node.value, end="\t")

        if node.right is not None:
            node.right.printBst()

    def contains(self, value):
        node = self
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def remove(self, value, parent=None):
        node = self
        while node is not None:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                if node.left is not None and node.right is not None:
                    node.value = node.right.getMinValue()
                    node.right.remove(node.value, node)
                elif parent is None:
                    if node.left is not None:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right is not None:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        return None
                elif parent.left == node:
                    parent.left = node.left if node.left is not None else node.right
                elif parent.right == node:
                    parent.right = node.left if node.left is not None else node.right
                break
        return self

    def getMinValue(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.value


def validateBST(tree):
    return isBstValid(tree, float("-inf"), float("inf"))


def isBstValid(tree, minValue, maxValue):
    if tree is None:
        return True

    if tree.value > maxValue or tree.value < minValue:
        return False
    return isBstValid(tree.left, minValue, tree.value) and isBstValid(tree.right, tree.value, maxValue)


def minHeightBst(array, startIdx, endIdx):
    if startIdx > endIdx:
        return None
    mid = (startIdx + endIdx) // 2
    bst = BST(array[mid])
    bst.left = minHeightBst(array, startIdx, mid - 1)
    bst.right = minHeightBst(array, mid + 1, endIdx)

    return bst


def invertBinaryTree(tree):
    que = [tree]
    while len(que):
        node = que.pop()
        if node is None:
            continue
        node.left, node.right = node.right, node.left
        que.extend([node.left, node.right])

def invertBstRecursive(tree):
    if tree is None:
        return
    invertBstRecursive(tree.left)
    invertBstRecursive(tree.right)
    tree.left, tree.right = tree.right, tree.left

def maxSubsetSumNoAdjacent(array):
    if len(array) < 1:
        return 0
    if len(array) == 2:
        return max(array[0], array[1])
    
    first = array[0]
    second = max(array[0], array[1])
    
    for i in range(2, len(array)):
        curr = array[i]
        curr = max( (curr + first) , second)
        first = second
        second = curr

def kadane(array):
    maxCurr = maxGlobal = float("-inf")
    for num in array:
        maxCurr = max( num, num + maxCurr )
        maxGlobal = max(maxCurr, maxGlobal)
    return maxGlobal


if __name__ == "__main__":

    # arr = [12, 3, 1, 2, -6, 5, -8, 6]
    # targetSum = 0
    # print(threeSum(arr, targetSum))

    # Doubly Linked List
    # ll = DoublyLinkedList()
    # ll.setHead(Node(1))
    # node = Node(3)
    # ll.insertAfter(ll.head, node)
    # ll.insertBefore(ll.tail, Node(2))

    # ll.insertAtPosition(4, Node(4))
    # ll.setHead(Node(-100))
    # ll.setTail(Node(100))

    # ll.removeNodeWithValue(4)
    # ll.remove(node)

    # ll.tail = ll.head

    # ll.printList()

    # sArray = [[1, 2, 3, 4],
    #           [12, 13, 14, 5],
    #           [11, 16, 15, 6],
    #           [10, 9, 8, 7]]

    # print(spiralTraverse(sArray))
    # array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    # print(f'The lonest Peak for {array} is : {longestPeak(array)}')

    # arr1 = [-1, 5, 10, 20, 28, 3]
    # arr2 = [26, 134, 135, 15, 17]
    # print(f'The smallest pair is: {smallestDifference(arr1, arr2)}')

    # array = [2, 1, 2, 2, 2, 3, 4, 2]
    # moveElementsToEnd(array, 2)
    # print(array)

    # print(isMonotnicArray([4,3, 2, 0]))

    # myBst = BST(50)
    # myBst.insert(25)
    # myBst.insert(10)
    # myBst.insert(30)

    # myBst.insert(75)
    # myBst.insert(60)
    # myBst.insert(80)

    # print(myBst.contains(10))
    # myBst.remove(10)
    # myBst.remove(25)

    # myBst.printBst()

    # print(validateBST(myBst))
    
    # from binarytree import bst
    # myBst = bst(2, is_perfect=True)

    # print(myBst)
    # invertBinaryTree(myBst)
    # print(myBst)
    
    # print(myBst)
    # invertBstRecursive(myBst)
    # print(myBst)

    # print(kadane([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))