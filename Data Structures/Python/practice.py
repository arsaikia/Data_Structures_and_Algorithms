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


def getArrivalTime(time, waitTime):
    if time > 100:
        hours = int(time / 100)
        minutes = int(time % 100)
    else:
        hours = 0
        minutes = time
    timeAfterWait = minutes + waitTime

    if timeAfterWait >= 60:
        additionalHours = int(timeAfterWait / 60)
        additionalMinutes = timeAfterWait % 60
        return ((((hours + additionalHours) % 24) * 100) + additionalMinutes)
    else:
        return ((hours % 24) * 100) + timeAfterWait


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
import heapq
class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = []
        self.greaters = []
        self.median = None

    def insert(self, number):
        if not len(self.lowers) or number < self.lowers[0]:
            heapq.heappush(self.lowers, number)
            print(self.lowers)
        else:
            heapq.heappush(self.greaters, number)
        self.rebalanceHeaps()
        
        self.updateMedian()
    
    def rebalanceHeaps(self):
        heapq.heapify(self.lowers)
        heapq.heapify(self.greaters)
        
        if len(self.lowers) - len(self.greaters) == 2:
            heapq.heappush(self.greaters, heapq.heappop(self.lowers))

        elif  len(self.greaters) - len(self.lowers) == 2:
            heapq.heappush(self.lowers, heapq.heappop(self.greaters))

    def updateMedian(self):
        if len(self.lowers) == len(self.greaters):
            self.median = ((self.lowers[0] + self.greaters[0])) / 2
        elif len(self.lowers) > len(self.greaters):
            self.median = self.lowers[0]
        else:
            self.median = self.greaters[0]

    def getMedian(self):
        return self.median

    def printHeap(self):
        pass
        # return self.lowers.printHeap(), self.greaters.printHeap()


class Heap:
    def __init__(self, array, comparisonFunc):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def printHeap(self):
        pass
        # print(self.heap)
        
    def buildHeap(self, array):
        firstParentIdx = len(array)-2 // 2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(array, currentIdx, len(array)-1)
        return array

    def siftDown(self, heap, currentIdx, endIdx):
        childOneIdx = (currentIdx*2) + 1
        while childOneIdx < endIdx:
            childTwoIdx = (currentIdx*2) + \
                2 if (currentIdx*2) + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            if self.comparisonFunc(heap[currentIdx], heap[idxToSwap]):
                self.swap(heap, currentIdx, idxToSwap)
                currentIdx = idxToSwap
                childOneIdx = (currentIdx*2)+1
            else:
                return

    def siftUp(self, heap, currentIdx):
        parentIdx = (currentIdx-1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(heap, currentIdx, parentIdx)
                currentIdx = parentIdx
                parentIdx = (currentIdx-1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap)-1)
        toRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(self.heap, 0, len(self.heap)-1)
        return toRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.heap, self.length - 1)

    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]
        return


def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b


C = ContinuousMedianHandler()

C.insert(5)
C.insert(10)
C.insert(100)
print(C.getMedian())
C.insert(200)
print(C.getMedian())

C.printHeap()


import heapq
x = heapq.heapify([2, 1, 12, -10, 100])
print(x)

