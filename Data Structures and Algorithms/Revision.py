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


# ----------------------------------------< BINARY SEARCH >------------------------------------------------------------
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


# ----------------------------------------< Find Three Largest Numbers >-----------------------------------------------
# O(n) Time | O(1) Space
def findThreeLargest(array):
    threeLargest = [float("-inf") for _ in range(3)]
    for num in array:
        if num > threeLargest[2]:
            insertAndShift(threeLargest, num, 2, threeLargest)
        elif num > threeLargest[1]:
            insertAndShift(threeLargest, num, 1, threeLargest)
        elif num > threeLargest[0]:
            insertAndShift(threeLargest, num, 0, threeLargest)
    return threeLargest


def insertAndShift(array, num, idx, threeLargest):
    i = 0
    while i <= idx:
        if i == idx:
            threeLargest[idx] = num
        else:
            threeLargest[i] = threeLargest[i + 1]
        i += 1

# ----------------------------------------< Bubble Sort >-----------------------------------------------
# WORST and Average: O(n^2) Time | O(1) Space
# Best: O(n) Time | O(1) Space


def bubbleSort(array):
    isSorted = True
    for i in reversed(range(len(array))):
        for j in range(1, i + 1):
            if array[j - 1] > array[j]:
                swap(array, j - 1, j)
                isSorted = False
        if isSorted:
            break
    return array


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# ----------------------------------------< Selection Sort >-----------------------------------------------
# O(n^2) Time | O(1) Space
def selectionSort(array):
    isSorted = True
    for i in reversed(range(len(array))):
        maxIdx = 0
        for j in range(1, i + 1):
            if array[j] > array[maxIdx]:
                maxIdx = j
                isSorted = False
        if maxIdx != i:
            swap(array, maxIdx, i)

        if isSorted:
            break
        
    return array

# ----------------------------------------< Insertion Sort >-----------------------------------------------
# O(n^2) time | O(1) Space
def insertionSort( array ):
    for i in range(1, len(array)):
        idx = i
        val = array[idx]
        while idx - 1 >= 0 and array[idx - 1] > val:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = val
    return array

# ----------------------------------------< Palindrome Chcek >-----------------------------------------------
# O(n) Time | O(1) Space
def checkPalindrome(string) -> bool :
    start, end = 0, len(string) - 1
    while start <= end:
        if string[start].lower() != string[end].lower():
            return False
        start += 1
        end -= 1
    return True

# ----------------------------------------< Ceaser Cypher Encryptor >-----------------------------------------
# O(n) Time | O(n) Space
def ceaserCypherEncryptor(string, k):
    charList = list(string)
    key = k & 26
    for idx, ch in enumerate(charList):
        charList[idx] = getEncrypted(ch, key)
    return "".join(charList)
    
def getEncrypted(char, key):
    code = ord(char) + key
    return chr(code) if code <= 122 else chr((code % 122) + 96)    



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

    '''Binary Search'''
    # array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    # target = 33
    # print(binarySearch(array, target))

    '''Find Three Largest Numbers'''
    # arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    # print(findThreeLargest(arr))

    '''SORT'''
    # print(bubbleSort([2, 10, 4, 8, -12, 13, -14]))
    # print(selectionSort([2, 10, 4, 8, -12, 13, -14]))
    # print(insertionSort([2, 10, 4, 8, -12, 13, -14]))
    
    '''Palindrome Check'''
    # print(checkPalindrome("aA"))
    
    '''Ceaser Cypher Encoder'''
    string = "xyz"
    key = 2
    print(ceaserCypherEncryptor(string, key))
    
