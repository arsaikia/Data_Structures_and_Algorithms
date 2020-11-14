# --------------------------------------<  Two Sum  >---------------------------------

# O(n) Time | O(n) Space
from random import getrandbits
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

# O(n) Time | O(log n) Space


def treeDepth(tree: binarytree) -> int:
    depth = [0]
    currentDepth = -1
    getDepths(tree, depth, currentDepth)
    return depth[0]


def getDepths(node: binarytree, depth: List[int], currentDepth: int) -> int:
    if node is None:
        return
    currentDepth += 1
    if node.left is None and node.right is None:
        depth[0] += currentDepth
    getDepths(node.left, depth, currentDepth)
    getDepths(node.right, depth, currentDepth)


class GraphNode:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(GraphNode(name))
        return self

    def DFS(self, array):
        array.append(self.name)
        for child in self.children:
            child.DFS(array)

# O(2 ^ n) Time | O(n) Space


def naiveFib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return naiveFib(num - 1) + naiveFib(num - 2)

# O(n) Time | O(n) Space


def memoizedFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = memoizedFib(n - 1, memoize) + memoizedFib(n - 2, memoize)
        return memoize[n]

# O(n) Time | O(1) Space


def optimizedFib(n):
    memo = [0, 1]
    getFib(n, 3, memo)
    return memo[1] if n > 1 else memo[0]


def getFib(n, k, memo):
    if k <= n:
        memo[0], memo[1] = memo[1], (memo[0] + memo[1])
        getFib(n, k + 1, memo)


# O(n) Time | O(d) d: Maximum depth of a special array
def productSum(array):
    return getProductSum(array, 1)


def getProductSum(array, depth):
    sum = 0
    for num in array:
        if type(num) == int:
            sum += num
        elif type(num) == list:
            sum += getProductSum(num, depth + 1)
    return sum * depth


# O(n) Time | O(log n) Space
def binarySearch(array, target):
    startIdx, endIdx = 0, len(array) - 1
    while startIdx <= endIdx:
        midIdx = (startIdx + endIdx) // 2
        potential = array[midIdx]
        if potential == target:
            return midIdx
        elif target > potential:
            startIdx = midIdx + 1
        elif target < potential:
            endIdx = midIdx - 1
    return -1


# O(n) Time | O(1) Space
def palindromeCheck(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

# O(n) Time | O(n) Space
def ceaserCypher( string, key ):
    opArray = list(string)
    key = key % 26

    for idx, val in enumerate(opArray):
        opArray[idx] = getEncrypted(val, key)

    return "".join(opArray)
    
def getEncrypted(val, key):
    currKey = key + ord(val)
    return chr(currKey) if currKey <= 122 else chr( (currKey % 122) + 96)  



if __name__ == "__main__":
    from binarytree import bst as tree
    bstTree = tree(is_perfect=True)
    print(bstTree)
    # print(findClosestValueInBst(bstTree, 17))

    # print(branchSums(bstTree))

    # num = 20
    # print(memoizedFib(num) == optimizedFib(num) == naiveFib(num))

    # print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))

    # print(binarySearch([1, 3, 5, 7, 12, 19, 21], 4))

    # print(palindromeCheck('ababa'))

    print(ceaserCypher('xyz', 2))