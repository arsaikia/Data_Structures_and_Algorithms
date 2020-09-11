'''
Algoexpert Easy poblems
'''

from functools import lru_cache
from typing import List


# ----------------------------------------< TWO SUM >-------------------------------------------------------

# Naive Two sum
# O(n^2) Time | O(1) Space (excluding Results array)
def naiveTwoSum(array: List[int], target: int) -> List[List]:
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                result.append([array[i], array[j]])
    return result

# O(nlogn) Time | O(1) Space


def twoPointerTwoSum(array: List[int], target: int) -> List[List]:
    # To use two pointer method, we need to sort the array
    array.sort()        # O(nlog(n)) Time | O(n log n) Space
    leftPtr, rightPtr = 0, len(array) - 1
    result = []
    while leftPtr < rightPtr:
        if array[leftPtr] + array[rightPtr] == target:
            result.append([array[leftPtr], array[rightPtr]])
            leftPtr += 1
            rightPtr -= 1
        elif array[leftPtr] + array[rightPtr] > target:
            rightPtr -= 1
        else:
            leftPtr += 1
    return result

# O(n) Time | O(n) Space


def twoSum(array: List[int], target: int) -> List[List]:
    complements = {}
    result = []
    for num in array:
        required = target - num
        if required in complements:
            result.append([num, required])
        else:
            complements[num] = True
    return result


# ----------------------------------------< Validate Subsequence >------------------------------------------
# O(n) Time | O(1) Space
def validateSubsequence(array, sequence) -> bool:
    arrIdx, seqIdx = 0, 0
    while seqIdx < len(sequence) and arrIdx < len(array):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# ----------------------------------------< Find Cosest value in BST >--------------------------------------


# Average: O(log n) Time | O(log n) Space : BALANCED TREE
# Worst : O(n) Time | O(n) Space  : UNBALANCED TREE
def findClosest(tree, target):
    return findClosestHelper(tree, float("inf"), target)


def findClosestHelper(node, closest, target):
    if node is None:
        return closest
    if abs(node.value - target) < abs(closest - target):
        closest = node.value
    if target < node.value:
        return findClosestHelper(node.left, closest, target)
    elif target > node.value:
        return findClosestHelper(node.right, closest, target)
    else:
        return closest


# ----------------------------------------< Branch Sums >--------------------------------------
# O(n) Time | O(n) Space
# The space is because imagine a tree with one root and every other node is leaf
def branchSums(tree):
    sums = []
    getBranchSums(tree, 0, sums)
    return sums


def getBranchSums(node, runningSum, sums):
    if node is None:
        return
    runningSum += node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)
    getBranchSums(node.left, runningSum, sums)
    getBranchSums(node.right, runningSum, sums)


# ----------------------------------------< Node Depths >--------------------------------------
# O(n) Time | O(1) Space
def nodeDepths(tree):
    return getNodeDepths(tree, 0)


def getNodeDepths(node, depth):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return depth
    depth += 1
    return getNodeDepths(node.left, depth) + getNodeDepths(node.right, depth)


# ----------------------------------------< DFS >-----------------------------------------------
# O(V + E) Time | O(V) Space
class MyNode:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(MyNode(name))
        return self

    def depthFirstSearch(self, array):
        node = [self]
        while len(node):
            curr = node.pop()
            array.append(curr.name)
            for child in curr.children:
                child.depthFirstSearch(array)
        return array


# ----------------------------------------< FIBONACCI >-----------------------------------------------
# O(2^n) Time | O(n) Time
def naiveFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return naiveFib(n - 1) + naiveFib(n - 2)


# O(N) Time | O(N) Space


@lru_cache
def memoizedFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return naiveFib(n - 1) + naiveFib(n - 2)


def memoizedFibonacci(n, memo={1: 0, 2: 1}):
    if n in memo:
        return memo[n]

    memo[n] = naiveFib(n - 1) + naiveFib(n - 2)
    return memo[n]


def fib(n):
    lastTwo = [0, 1]
    k = 3
    while k <= n:
        lastTwo[0], lastTwo[1] = lastTwo[1], (lastTwo[0] + lastTwo[1])
        k += 1

    return lastTwo[-1] if k > 1 else lastTwo[0]

# ----------------------------------------< PRODUCT SUM >-----------------------------------------------
# O(n) Time | O(d) Space where d is the max depth -> stack frames


def productSum(nums):
    return getProductSums(nums, 1)


def getProductSums(nums, depth):
    sum = 0
    for num in nums:
        if type(num) == list:
            sum += getProductSums(num, depth + 1)
        else:
            sum += num
    return depth * sum


# ----------------------------------------< BINARY SEARCH >-----------------------------------------------
# O(nlog(n)) Time | O(nlog(n)) Space
def binarySearch(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    '''2SUM'''
    # array = [2, -1, 4, 6, 10, 13]
    # target = 12
    # print(naiveTwoSum(array, target))
    # print(twoPointerTwoSum(array, target))
    # print(twoSum(array, target))

    '''validateSubsequence'''
    # arr = [5, 1, 22, 25, 6, -1, 8, 10]
    # seq = [1, 6, -1, 10]
    # print(validateSubsequence(arr, seq))

    '''findClosest'''
    # from binarytree import Node
    # tree = Node(10)
    # tree.left = Node(5)
    # tree.left.left = Node(2)
    # tree.left.left.left = Node(1)
    # tree.left.right = Node(5)
    # tree.right = Node(15)
    # tree.right.left = Node(13)
    # tree.right.right = Node(22)
    # tree.right.left.right = Node(14)
    # target = 12
    # print(findClosest(tree, target))

    '''branchSums'''
    # print(branchSums(tree))

    '''nodeDepths'''
    # from binarytree import bst
    # tree = bst(3, True)
    # print(tree)
    # print(nodeDepths(tree))

    '''DFS'''
    # node = MyNode("A")
    # first = node.addChild("B")
    # first.addChild("E")
    # second = first.addChild("F").addChild("I")
    # second.addChild("J")
    # node.addChild("C")
    # third = node.addChild("D")
    # fourth = third.addChild("G")
    # fourth.addChild("K")
    # third.addChild("H")
    # arr = []
    # node.depthFirstSearch(arr)
    # print(arr)

    '''Naive Fib'''
    # print(naiveFib(18) == 1597)
    # print(memoizedFib(18) == memoizedFibonacci(18) == fib(18))

    '''Product Sums'''
    # nums = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    # print(productSum(nums))

    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binarySearch(array, target))
    
