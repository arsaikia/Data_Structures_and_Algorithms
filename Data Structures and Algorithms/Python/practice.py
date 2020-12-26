# # Fibonnaci
# import time as t
# # Naive

# def Naivefib( n ):
#     if n == 1: return 0
#     elif n == 2: return 1
#     else: return Naivefib(n-1) + Naivefib(n-2)

# def Memoizedfib( n , memo={1:0, 2: 1}):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = Memoizedfib(n-1, memo) + Memoizedfib(n-2, memo)
#         return memo[n]

# def BottomUpFib( n ):
#     firstTwo = [0, 1]
#     counter = 3
#     while counter <= n:
#         value = firstTwo[0] + firstTwo[1]
#         firstTwo[0], firstTwo[1] = firstTwo[1], value
#         counter += 1
#     return firstTwo[1] if n>1 else firstTwo[0]

# num = 30
# start = t.time()
# val = Naivefib(num)
# end = t.time()
# print(f'Naive Fib of {num} is {val} which takes {end-start} seconds!')

# start = t.time()
# val = Memoizedfib(num)
# end = t.time()
# print(f'Memoizedfib of {num} is {val} which takes {end-start} seconds!')

# start = t.time()
# val = BottomUpFib(num)
# end = t.time()
# print(f'BottomUpFib of {num} is {val} which takes {end-start} seconds!')

# '''
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULTS>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Naive Fib   of 30 is 514229 which takes 0.1816  seconds!
# Memoizedfib of 30 is 514229 which takes 0.0000  seconds!
# BottomUpFib of 30 is 514229 which takes 0.0000  seconds!
# '''

# # Find closest in Binary Search tree

# def findClosest( tree, target ):
#     closest = float('inf')
#     return findClosestHelper(tree, target, closest)

# def findClosestHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(closest-target) > abs(tree.value - target):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestHelper(tree.right, target, closest)
#     else:
#         return closest


#   Find Numbers with Even Number of Digits
# from typing import List
# import math
# def findNumbers(nums: List[int]) -> int:
#     count = 0
#     for each in nums:
#         if math.ceil(math.log10(each)) != 0 and math.ceil(math.log10(each))%2 == 0:
#             count += 1
#     return count

# nums = [12,345,2,6,7896]

# print(findNumbers(nums))


'''
PRACTICE
'''
#  0  1  2  3   4   0+4//2=2->6
# [2, 4, 6, 8, 12]  --> 8
# array = [i for i in range(0, 20, 2)]
# for idx, num in enumerate(array):
#     print(idx, num)


# array = [1, 2, 3, 4, 5]

# print((len(array)+16) % len(array))


# string = "Id sit commodo anim labore amet amet voluptate ea."
# print(string.split(' ', 1))

# import random
# arr = ['let3 art zero', 'let1 art can', 'let5 art can', 'let2 own kit dig']
# x = sorted(arr, key=lambda k: (k.split(' ', 1)[1], k.split(' ', 1)[0]))
# print(x)

# x = [1, 2, 3]
# y = [4, 5, 6]
# x.extend(y)
# print(x)


# print(random.choice([12, 3, 4, -1, 2]))
# print(random.randint(0, 10))

# # O(N) time | O(1) Space


# def isMonotonic(array):
#     if len(array) < 2:
#         return True
#     return isIncreasing(array) or isDecreasing(array)


# def isIncreasing(arr):
#     for idx in range(1, len(arr)):
#         if arr[idx] < arr[idx-1]:
#             return False
#     return True


# def isDecreasing(arr):
#     for idx in range(1, len(arr)):
#         if arr[idx] > arr[idx-1]:
#             return False
#     return True


# print(1 in {1: True, 2: True, 3: True, 4: True})


# # Do not edit the class below except for
# # the insert, contains, and remove methods.
# # Feel free to add new properties and methods
# # to the class.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         curr = self
#         while True:
# 			if value < curr.value:
# 				if curr.left is None:
# 					curr.left = BST(value)
# 					break
# 				else:
# 					curr = curr.left
# 			else:
# 				if curr.right is None:
# 					curr.right = BST(value)
# 					break
# 				else:
# 					curr = curr.right
#         return self

#     def contains(self, value):
#         curr = self
#         while curr is not None:
# 			if value < curr.value:
# 				curr = curr.left
# 			elif value > curr.value:
# 				curr = curr.right
# 			else:
#                 return True
# 	    return False

#     def remove(self, value, parent = None):
#         curr = self
#         while curr is not None:
# 			if value < curr.value:
# 				parent = curr
# 				curr = curr.left
# 			elif value > curr.value:
# 				parent = curr
# 				curr = curr.right
# 			else:
# 				if curr.left is not None and curr.right is not None:
# 					curr.value = curr.right.getMinValue()
# 					curr.right.remove(curr.value, curr)
# 				elif parent is None:
# 					if curr.left is not None:
# 						curr.value = curr.left.value
# 						curr.right = curr.left.right
# 						curr.left = curr.left.left
# 					elif curr.right is not None:
# 						curr.value = curr.right.value
# 						curr.left = curr.right.left
# 						curr.right = curr.right.right
# 					else:
# 						curr = None
# 				elif parent.left == curr:
# 					parent.left = curr.left if curr.left is not None else curr.right
# 				elif parent.right == curr:
# 					parent.left = curr.left if curr.left is not None else curr.right
# 				break
#         return self

# 	def getMinValue(self):
# 		curr = self
# 		while curr.left is not None:
# 			curr = curr.left
#    		return curr.value


# class TreeNode:
# 	def __init__(self, x):
# 		self.value = x
# 		self.left = None
# 		self.right = None

# Tree = TreeNode(10)
# Tree.left = TreeNode(5)
# Tree.right = TreeNode(2)
# Tree.left.left = TreeNode(12)
# Tree.left.right = TreeNode(9)
# Tree.right.left = TreeNode(7)
# Tree.right.right = TreeNode(11)


# def printTree(node):
#     if node is None:
#        return
#     print(node.value)
#     printTree(node.left)
#     printTree(node.right)

# def getNodeRoute(node, runningValues, target):
#     if node is None:
#         return
#     newRunningValues = runningValues + [node.value]
#     if node.value == target:
#         return newRunningValues
#     return getNodeRoute(node.left, newRunningValues, target)
#     return getNodeRoute(node.left, newRunningValues, target)


# printTree(Tree)
# print(getNodeRoute(Tree, [], 12))


# def sameBsts(arrayOne, arrayTwo):
#     if arrayOne[0] != arrayTwo[0] or len(arrayOne) != len(arrayTwo):
#         return False

#     arr1 = [arrayOne[0]]
#     rootIdx = 0

#     for i in range(1, len(arrayOne)):
#         idx = rootIdx
#         print(arrayOne[i], arr1[idx])
#         if arrayOne[i] < arr1[idx]:
#             while (idx != 0 or idx != len(arr1)-1) or arrayOne[i] < arr1[idx]:
#                 idx -= 1
#             arr1.popleft(arrayOne[i])
#             idx += 1
#             continue
#     print(arr1)


# sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81])
# arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
# leftOne = [arrayOne[i]
#            for i in range(1, len(arrayOne)) if arrayOne[i] < arrayOne[0]]
# rightOne = [arrayOne[i] for i in range(1, len(arrayOne)) if arrayOne[i] >= arrayOne[0]]


# from itertools import permutations
# import heapq


# def getArrivalTime(time, waitTime):
#     if time > 100:
#         hours = int(time / 100)
#         minutes = int(time % 100)
#     else:
#         hours = 0
#         minutes = time
#     timeAfterWait = minutes + waitTime

#     if timeAfterWait >= 60:
#         additionalHours = int(timeAfterWait / 60)
#         additionalMinutes = timeAfterWait % 60
#         return ((((hours + additionalHours) % 24) * 100) + additionalMinutes)
#     else:
#         return ((hours % 24) * 100) + timeAfterWait


# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         startTimes = sorted([meeting[0] for meeting in intervals])
#         endTimes = sorted([meeting[1] for meeting in intervals])
#         start, end = 0, 0
#         occupiedRooms = 0

#         while start < len(startTimes) and end < len(endTimes):
#             meetingStarts = startTimes[start]
#             meetingEnds = endTimes[end]
#             if meetingStarts < meetingEnds:
#                 occupiedRooms += 1
#                 start += 1
#             else:
#                 start += 1
#                 end += 1

#         return occupiedRooms

# print(getArrivalTime(1259, 60))


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.


# class ContinuousMedianHandler:
#     def __init__(self):
#         self.lowers = []
#         self.greaters = []
#         self.median = None

#     def insert(self, number):
#         if not len(self.lowers) or number < self.lowers[0]:
#             heapq.heappush(self.lowers, number)
#             print(self.lowers)
#         else:
#             heapq.heappush(self.greaters, number)
#         self.rebalanceHeaps()

#         self.updateMedian()

#     def rebalanceHeaps(self):
#         heapq.heapify(self.lowers)
#         heapq.heapify(self.greaters)

#         if len(self.lowers) - len(self.greaters) == 2:
#             heapq.heappush(self.greaters, heapq.heappop(self.lowers))

#         elif len(self.greaters) - len(self.lowers) == 2:
#             heapq.heappush(self.lowers, heapq.heappop(self.greaters))

#     def updateMedian(self):
#         if len(self.lowers) == len(self.greaters):
#             self.median = ((self.lowers[0] + self.greaters[0])) / 2
#         elif len(self.lowers) > len(self.greaters):
#             self.median = self.lowers[0]
#         else:
#             self.median = self.greaters[0]

#     def getMedian(self):
#         return self.median

#     def printHeap(self):
#         pass
#         # return self.lowers.printHeap(), self.greaters.printHeap()


# class Heap:
#     def __init__(self, array, comparisonFunc):
#         self.comparisonFunc = comparisonFunc
#         self.heap = self.buildHeap(array)
#         self.length = len(self.heap)

#     def printHeap(self):
#         pass
#         # print(self.heap)

#     def buildHeap(self, array):
#         firstParentIdx = len(array)-2 // 2
#         for currentIdx in reversed(range(firstParentIdx+1)):
#             self.siftDown(array, currentIdx, len(array)-1)
#         return array

#     def siftDown(self, heap, currentIdx, endIdx):
#         childOneIdx = (currentIdx*2) + 1
#         while childOneIdx < endIdx:
#             childTwoIdx = (currentIdx*2) + \
#                 2 if (currentIdx*2) + 2 <= endIdx else -1
#             if childTwoIdx != -1:
#                 if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
#                     idxToSwap = childTwoIdx
#                 else:
#                     idxToSwap = childOneIdx
#             if self.comparisonFunc(heap[currentIdx], heap[idxToSwap]):
#                 self.swap(heap, currentIdx, idxToSwap)
#                 currentIdx = idxToSwap
#                 childOneIdx = (currentIdx*2)+1
#             else:
#                 return

#     def siftUp(self, heap, currentIdx):
#         parentIdx = (currentIdx-1) // 2
#         while currentIdx > 0:
#             if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
#                 self.swap(heap, currentIdx, parentIdx)
#                 currentIdx = parentIdx
#                 parentIdx = (currentIdx-1) // 2
#             else:
#                 return

#     def peek(self):
#         return self.heap[0]

#     def remove(self):
#         self.swap(self.heap, 0, len(self.heap)-1)
#         toRemove = self.heap.pop()
#         self.length -= 1
#         self.siftDown(self.heap, 0, len(self.heap)-1)
#         return toRemove

#     def insert(self, value):
#         self.heap.append(value)
#         self.length += 1
#         self.siftUp(self.heap, self.length - 1)

#     def swap(self, heap, i, j):
#         heap[i], heap[j] = heap[j], heap[i]
#         return


# def MAX_HEAP_FUNC(a, b):
#     return a > b


# def MIN_HEAP_FUNC(a, b):
#     return a < b


# C = ContinuousMedianHandler()

# C.insert(5)
# C.insert(10)
# C.insert(100)
# print(C.getMedian())
# C.insert(200)
# print(C.getMedian())
# C.printHeap()

# def countArrangement(N):
#     values = tuple(range(1, N+1))
#     return getValidArrangements(values, {})

# def getValidArrangements(arrangement, memo):
#         if len(arrangement) == 1:
#             return 1

#         if arrangement in memo:
#             return memo[arrangement]
#         total = 0
#         for j in range(len(arrangement)):
#             if isValid(arrangement, j):
#                 remaining = arrangement[:j] + arrangement[j+1:]
#                 print(remaining)
#                 total += getValidArrangements(remaining, memo)

#         memo[arrangement] = total
#         return total

# def isValid(array, idx):
#     return array[idx] % len(array) == 0 or len(array) % array[idx] == 0

# print(countArrangement(3))


# val = ord("z")+1
# print(chr(val) if val <= 122 else chr((val % 122) + 96) )

# -------------------------------------< HOW TO IMPORT A MODULE  >--------------------------------------
# from modules import bst
# import sys
# sys.path.insert(0, './modules/')

# BST = bst.BST

# binarySearchTree = BST(50)
# binarySearchTree.insert(20).insert(30).insert(5).insert(40).insert(1)
# binarySearchTree.printTree()
# -------------------------------------< HOW TO IMPORT A MODULE  >--------------------------------------

# import sys
# from modules import heap
# import numpy as np
# s1 = "BATD"
# s2 = "ABACD"
# m = len(s1) - 1
# n = len(s2) - 1


# def lcsRecursive(s1, s2, m, n):
#     if m < 0 or n < 0:
#         return 0

#     if s1[m] == s2[n]:
#         count = 1 + lcsRecursive(s1, s2, m - 1, n - 1)
#     else:
#         count = max(lcsRecursive(s1, s2, m - 1, n),
#                     lcsRecursive(s1, s2, m, n - 1))
#     return count


# memo = [[0 for col in range(len(s1) + 1)] for row in range(len(s2) + 1)]


# def lcsMemoizedRecursive(s1, s2, m, n, memo):
#     if m == 0 or n == 0:
#         return 0
#     if memo[m][n] != 0:
#         return memo[m][n]

#     if s1[n - 1] == s2[m - 1]:
#         count = 1 + lcsMemoizedRecursive(s1, s2, m - 1, n - 1, memo)
#     else:
#         count = max(lcsMemoizedRecursive(s1, s2, m - 1, n, memo),
#                     lcsMemoizedRecursive(s1, s2, m, n - 1, memo))
#     memo[m][n] = count
#     return count


# def trverseSubstring(string, memo):
#     sequence = []
#     row = len(memo) - 1
#     col = len(memo[0]) - 1
#     while row > 0 and col > 0:
#         if memo[row][col] == memo[row - 1][col]:
#             row -= 1
#         elif memo[row][col] == memo[row][col - 1]:
#             col -= 1
#         else:
#             sequence.append(string[row - 1])
#             row -= 1
#             col -= 1
#     return "".join(list(reversed(sequence)))


# def lcsBottomsUp(s1, s2):
#     cache = [[0 for col in range(len(s1) + 1)] for row in range(len(s2) + 1)]
#     for row in range(1, len(cache)):
#         for col in range(1, len(cache[0])):
#             if s2[row - 1] == s1[col - 1]:
#                 cache[row][col] = cache[row - 1][col - 1] + 1
#             else:
#                 cache[row][col] = max(cache[row][col - 1], cache[row - 1][col])
#     return cache[-1][-1]


# # print(lcsRecursive(s1, s2, m, n))
# print(lcsMemoizedRecursive(s1, s2, len(s2), len(s1), memo))
# print(trverseSubstring(s2, memo))
# print(np.array(lcsBottomsUp(s1, s2)))

# from modules import heap
# import sys
# sys.path.insert(0, './modules/')

# # O(n log(n)) time | O(1) Space
# def heapSort(array):
#     minHeap = heap.Heap(array)
#     for i in reversed(range(1, len(array))):
#         array[i], array[0] = array[0], array[i]
#         minHeap.siftDown(minHeap.heap, 0, i - 1)
#     return list(reversed(array))


# print(heapSort([-1, 21, 10, 8, 9, 12]))
import numpy as np
# items = [[1, 2], [4, 3], [5, 6], [6, 7]]
# capacity = 10
# idx = len(items) - 1
# memo = [[None for col in range(capacity)] for row in range(len(items))]

# # Top Down


# def knapsack(array, capacity, idx, memo):
#     if idx == 0 or capacity == 0:
#         return 0

#     if memo[idx][capacity - 1] is not None:
#         return memo[idx][capacity]

#     curr = array[idx]
#     value = curr[0]
#     weight = curr[1]

#     if capacity >= weight:
#         val = max(value + knapsack(array, capacity - weight, idx - 1, memo),
#                   knapsack(array, capacity, idx - 1, memo))
#     else:
#         val = knapsack(array, capacity, idx - 1, memo)

#     memo[idx][capacity - 1] = val
#     return val


# # print("Top Down", knapsack(items, capacity, idx, memo))


# def knapsackBottomUp(array, capacity):
#     cache = [[0 for col in range(capacity + 1)]
#              for row in range(len(items) + 1)]
#     for row in range(1, len(cache)):
#         for col in range(1, len(cache[0])):
#             value = array[row - 1][0]
#             weight = array[row - 1][1]

#             if weight > col:
#                 cache[row][col] = cache[row - 1][col]
#             else:
#                 cache[row][col] = max(cache[row - 1][col],
#                                       value + cache[row - 1][col - weight])

#     return cache[-1][-1]


# # print("Bottom Up", knapsackBottomUp(items, capacity))


# def solve(input):
#     res = [[None for _ in range(len(input[0]))] for row in input]
#     for i in reversed(range(len(input))):
#         for j in reversed(range(len(input[i]))):
#             diagonal_element = 0
#             if i > 0 and j > 0:
#                 diagonal_element = input[i-1][j-1]

#             up_row = 0
#             if i > 0:
#                 up_row = input[i-1][j]

#             prev_col = 0
#             if j > 0:
#                 prev_col = input[i][j-1]

#             res[i][j] = input[i][j] + diagonal_element - up_row - prev_col
#     return res


# arr = [[33, 94, 56, 34, 77], [89, 27, 55, 74, 3], [38, 20, 90, 45, 60], [98, 65, 58, 18, 14], [2, 64, 11, 1, 79], [4, 67, 78, 13, 53],
#        [98, 68, 90, 2, 62], [13, 1, 34, 75, 95], [23, 16, 39, 95, 42]]

# print(np.array(arr), "\n")
# print(np.array(solve(arr)))


# def transpose(matrix):

#     for row in range(len(matrix)):
#         for col in range(row + 1, len(matrix[0])):
#             matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

#     for row in range(len(matrix)):
#         for col in range(len(matrix[0]) // 2):
#             matrix[row][col], matrix[row][len(
#                 matrix[0]) - 1 - col] = matrix[row][len(matrix[0]) - 1 - col],  matrix[row][col]

#     return np.array(matrix, "\n")


# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), "\n")
# print(np.array([[7, 4, 1], [8, 5, 2], [9, 6, 3]]))

def knmuthMorrisPratt(string, substring):
    pattern = buildPattern(substring)
    # return doesMatch(string, substring, pattern)
    count = 0
    for i in range(0, len(string) - len(substring) + 1):
        # [i : i + len(substring)]
        if doesMatch(string, i, substring, pattern):
            count += 1
    return count


def buildPattern(substring):
    pattern = [-1 for _ in substring]
    i, j = 1, 0
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


def doesMatch(string, startIdx, substring, pattern):
    i, j = startIdx, 0
    while i <= startIdx + len(substring) - 1:
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False

testArray = [["01010101", "01", 4], [
    "0100010", "010", 2], ["00000000000", "00", 10]]
for test in testArray:
    print(test, knmuthMorrisPratt(test[0], test[1]) == test[2])




    if __name__ == "__main__":
        li = [1,2,3, 0, 0]
        print(li)
        li.pop()
        print(li)




