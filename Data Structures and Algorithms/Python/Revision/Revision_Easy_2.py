
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
def dfs(node, result):
    stack = [node]
    for each in stack:
        if each is None:
            continue
        result.append(each.value)
        dfs(each.left, result)
        dfs(each.right, result)
    





if __name__ == "__main__":
    import numpy as np

    twoSum = TwoSum()
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    print(twoSum.twoSum(array, target))
    print(twoSum.twoSumSorted(array, target))
    print(twoSum.twoSumSumOptimized(array, target))

    checkSubsequence = ValidateSubsequence()
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(checkSubsequence.isSubsequence(array, sequence))

    closestInBst = ClosestValueInBST()
    bst = Node(10)
    bst.left = Node(5)
    bst.left.left = Node(2)
    bst.left.right = Node(5)
    bst.left.left.left = Node(1)
    bst.right = Node(15)
    bst.right.left = Node(13)
    bst.right.right = Node(22)
    bst.right.left.right = Node(14)
    print(bst)
    print(closestInBst.findClosest(bst, 12))

    branchSums = BranchSums()
    branchSums.findSums(bst, 0)
    print(branchSums.getSums())
    
    print(nodeDepth(bst, 0))
    
    result = []
    dfs(bst, result)
    print(result)
