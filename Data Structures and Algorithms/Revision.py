'''
Algoexpert Easy poblems
'''

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


if __name__ == "__main__":
    # array = [2, -1, 4, 6, 10, 13]
    # target = 12
    # print(naiveTwoSum(array, target))
    # print(twoPointerTwoSum(array, target))
    # print(twoSum(array, target))

    # arr = [5, 1, 22, 25, 6, -1, 8, 10]
    # seq = [1, 6, -1, 10]
    # print(validateSubsequence(arr, seq))

    from binarytree import Node
    tree = Node(10)
    tree.left = Node(5)
    tree.left.left = Node(2)
    tree.left.left.left = Node(1)
    tree.left.right = Node(5)
    tree.right = Node(15)
    tree.right.left = Node(13)
    tree.right.right = Node(22)
    tree.right.left.right = Node(14)
    target = 12
    print(findClosest(tree, target))
