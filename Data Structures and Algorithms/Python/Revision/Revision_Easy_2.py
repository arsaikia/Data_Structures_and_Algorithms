
from typing import List
from binarytree import Node

# --------------------------------------<  TWO SUM  >----------------------------------------------


class TwoSum:
    def __init__(self) -> List[int]:
        self.result = []

    # O(n^2) Time | O(n^2) Space
    def twoSum(self, array: List[int], target: int) -> List[int]:
        self.result = []
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == target:
                    self.result.append([array[i], array[j]])
        return self.result

    # O(n log(n)) Time | O(nlog(n)) Space
    def twoSumSorted(self, array: List[int], target: int) -> List[int]:
        self.result = []
        array.sort()
        start, end = 0, len(array) - 1
        while start < end:
            firstNum = array[start]
            secondNum = array[end]
            if firstNum + secondNum > target:
                end -= 1
            elif firstNum + secondNum < target:
                start += 1
            else:
                self.result.append([firstNum, secondNum])
                start += 1
                end -= 1
        return self.result

    # O(n) tim | O(n) Space
    def twoSumSumOptimized(self, array: List[int], target: int) -> List[int]:
        self.result = []
        visited = set()
        for num in array:
            required = target - num
            if required in visited:
                self.result.append([num, required])
            else:
                visited.add(num)
        return self.result

# --------------------------------------<  VALIDATE SUBSEQUENCE  >---------------------------------


class ValidateSubsequence:
    def __init__(self) -> None:
        pass

    # O(n) Time | O(1) Space
    def isSubsequence(self, array, sequence):
        arrayIdx = sequenceIdx = 0
        while arrayIdx < len(array) and sequenceIdx < len(sequence):
            if array[arrayIdx] == sequence[sequenceIdx]:
                arrayIdx += 1
                sequenceIdx += 1
            else:
                arrayIdx += 1
        return sequenceIdx == len(sequence)

# --------------------------------------<  Closest Value in BST  >---------------------------------
# Average: O(d) Time | O(d) Space
# Worst: O(n) Time | O(n) Space


class ClosestValueInBST:
    def __init__(self):
        self.closest = float("inf")

    def findClosest(self, bst, target) -> int:
        if bst is None:
            return self.closest
        if abs(bst.value - target) < abs(target - self.closest):
            self.closest = bst.value
        if target < bst.value:
            return self.findClosest(bst.left, target)
        else:
            return self.findClosest(bst.right, target)

# --------------------------------------<  Branch Sums  >---------------------------------

# O(n) Time | O(n) Space


class BranchSums:
    def __init__(self) -> List[int]:
        self.sums = []

    def findSums(self, tree, runningSum):
        if tree is None:
            return
        runningSum += tree.value
        if tree.left is None and tree.right is None:
            self.sums.append(runningSum)
        self.findSums(tree.left, runningSum)
        self.findSums(tree.right, runningSum)

    def getSums(self):
        return self.sums

# --------------------------------------<  Node Depth  >---------------------------------

# O(n) Time | O(d) Space


def nodeDepth(tree, depth) -> int:
    if tree is None:
        return 0
    return depth + nodeDepth(tree.left, depth + 1) + nodeDepth(tree.right, depth + 1)


# --------------------------------------<  DFS  >---------------------------------
# O(v+e) Time | O(v) Space
def dfs(node, result):
    stack = [node]
    for each in stack:
        if each is None:
            continue
        result.append(each.value)
        dfs(each.left, result)
        dfs(each.right, result)

# --------------------------------------<  FIBONACCI  >---------------------------------
# O(n) Time | O(1) Space


def fib(n):
    values = [0, 1]
    for _ in range(3, n+1):
        values[0], values[1] = values[1], (values[0] + values[1])
    return values[1] if n > 1 else values[0]


# --------------------------------------<  PRODUCT SUM  >---------------------------------
# O(logn) Time | O(1) Space
def productSumWithDepth(array, depth):
    sum = 0
    for each in array:
        if type(each) is list:
            sum += productSumWithDepth(each, depth+1)
        else:
            sum += each
    return sum * depth

# --------------------------------------<  BINARY SEARCH  >---------------------------------
# O(logn) Time | O(1) Space


def binarySearch(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

# --------------------------------------<  Find Three largest Numbers  >---------------------------------


def findThreeLargestNumbers(array):
    threeLargest = [float("-inf") for _ in range(3)]
    for num in array:
        getThreeLargest(num, threeLargest)
    return threeLargest


def getThreeLargest(num, largest):
    if num > largest[2]:
        shiftAndUpdate(largest, num, 2)
    elif num > largest[1]:
        shiftAndUpdate(largest, num, 1)
    elif num > largest[0]:
        shiftAndUpdate(largest, num, 0)


def shiftAndUpdate(largest, value, idx):
    for i in range(idx + 1):
        if i == idx:
            largest[i] = value
        else:
            largest[i] = largest[i + 1]


if __name__ == "__main__":
    import numpy as np

    # twoSum = TwoSum()
    # array = [3, 5, -4, 8, 11, 1, -1, 6]
    # target = 10
    # print(twoSum.twoSum(array, target))
    # print(twoSum.twoSumSorted(array, target))
    # print(twoSum.twoSumSumOptimized(array, target))

    # checkSubsequence = ValidateSubsequence()
    # array = [5, 1, 22, 25, 6, -1, 8, 10]
    # sequence = [1, 6, -1, 10]
    # print(checkSubsequence.isSubsequence(array, sequence))

    # closestInBst = ClosestValueInBST()
    # bst = Node(10)
    # bst.left = Node(5)
    # bst.left.left = Node(2)
    # bst.left.right = Node(5)
    # bst.left.left.left = Node(1)
    # bst.right = Node(15)
    # bst.right.left = Node(13)
    # bst.right.right = Node(22)
    # bst.right.left.right = Node(14)
    # print(bst)
    # print(closestInBst.findClosest(bst, 12))

    # branchSums = BranchSums()
    # branchSums.findSums(bst, 0)
    # print(branchSums.getSums())

    # print(nodeDepth(bst, 0))

    # result = []
    # dfs(bst, result)
    # print(result)

    # print(fib(6))

    # array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    # print(productSumWithDepth( array, 1 ))

    # arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    # target = 33
    # print(binarySearch(arr, target))

    print(findThreeLargestNumbers(
        [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
