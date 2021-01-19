from binarytree import bst
from typing import List

# ? Naive Two Sum
# O(n^2) Time | O(1) Space


def twoSum(arr: List[int], target: int) -> List[int]:
    for i in range(len(arr)):   # O(n) Time
        firstNum = arr[i]
        for j in range(i + 1, len(arr)):    # O(n) Time
            secondNum = arr[j]
            if firstNum + secondNum == target:
                return [i, j]

    return [-1, -1]

# ? Sort and find
# O(n log n) Time | O(n log n) Space


def sortAndFind(arr: List[int], target: int) -> List[int]:

    indices = {num: idx for idx, num in enumerate(arr)}

    # -1, 1, 2, 3, 4, 6, 9
    arr.sort()  # O(n log n)
    start, end = 0, len(arr) - 1
    while start < end:
        leftNum = arr[start]
        rightNum = arr[end]
        if leftNum + rightNum == target:
            return [indices[leftNum], indices[rightNum]]
        elif leftNum + rightNum > target:
            end -= 1
        else:
            start += 1
    return [-1, -1]


# ? Two pointers
def twoPointers(arr: List[int], target: int) -> List[int]:
    visited = {}

    for idx, num in enumerate(arr):
        required = target - num
        if required in visited:
            return [visited[required], idx]
        else:
            visited[num] = idx
    return [-1, -1]


def validateSubsequence(arr, sub):
    arrIdx = 0
    subIdx = 0
    while arrIdx < len(arr) and subIdx < len(sub):
        if arr[arrIdx] == sub[subIdx]:
            arrIdx += 1
            subIdx += 1
        else:
            arrIdx += 1
    return subIdx == len(sub)


def findClosest(node, target):
    closest = float('inf')
    return getClosest(node, target, closest)


def getClosest(node, target, closest):
    if node is None:
        return closest

    if abs(node.value - target) < abs(closest - target):
        closest = node.value

    if target < node.value:
        return getClosest(node.left, target, closest)
    elif target > node.value:
        return getClosest(node.right, target, closest)
    else:
        return closest


def branchSums(tree):
    sums = []
    getBranchSums(tree, 0, sums)
    return sums


def getBranchSums(tree, runningSum, sums):
    if tree is None:
        return 0

    runningSum += tree.value
    if tree.left is None and tree.right is None:
        sums.append(runningSum)

    getBranchSums(tree.left, runningSum, sums)
    getBranchSums(tree.right, runningSum, sums)


def nodeDepth(tree):
    return getDepthSum(tree, 0)


def getDepthSum(tree, depth):
    if tree is None:
        return 0

    return getDepthSum(tree.left, depth + 1) + getDepthSum(tree.right, depth + 1) + depth


# print(twoPointers([1, 2, 4, 6, 3, 9, -1], 12))
# print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
myTree = bst(2, True)
print(myTree)
# print(findClosest(myTree, -112))
# print(branchSums(myTree))

print(nodeDepth(myTree))
