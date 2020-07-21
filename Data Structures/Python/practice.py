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


def twoSum(array, target):
    if len(array) == 0:
        return -1

    elemDict = {}
    for idx, each in enumerate(array):
        print(idx, elemDict)
        required = target-each
        if required in elemDict:
            return [idx, elemDict[required]]
        else:
            elemDict[each] = idx
    return -1


print(twoSum([2, 4, 6, 8, 12], 12))
