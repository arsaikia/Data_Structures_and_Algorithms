# --------------------------------------<  Two Sum  >---------------------------------

# O(n) Time | O(n) Space
from typing import List
import binarytree


def twoSum(array, target):

    visited = {}

    for idx, num in enumerate(array):
        required = target - num
        if required in visited:
            return True
        else:
            visited[num] = idx
    return False


# O(n) Time | O(1) Space
def validateSubsequence(array, sequence):
    arrayIdx = sequenceIdx = 0

    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)


# Average:  O(n log n) | O(log n) Space
# Worst:    O(n) | O(n) Space
def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, float("inf"))


def findClosestValueHelper(node, target, closest):
    if node is None:
        print(node, closest)
        return closest
    if abs(node.value - target) < abs(target - closest):
        closest = node.value
    if target > node.value:
        return findClosestValueHelper(node.right, target, closest)
    elif target < node.value:
        return findClosestValueHelper(node.left, target, closest)
    else:
        return closest


# O(n) Time | O(n) Space
def branchSums(tree: binarytree) -> List[int]:
    sums = []
    runningSum = 0
    getBranchSums(tree, sums, runningSum)
    return sums


def getBranchSums(node: binarytree, sums: List[int], runningSum: int) -> List[int]:
    if node is None:
        return

    runningSum += node.val

    if node.left is None and node.right is None:
        sums.append(runningSum)
    getBranchSums(node.left, sums, runningSum)
    getBranchSums(node.right, sums, runningSum)


if __name__ == "__main__":
    from binarytree import bst as tree
    bstTree = tree(is_perfect=True)
    print(bstTree)
    # print(findClosestValueInBst(bstTree, 17))

    print(branchSums(bstTree))
