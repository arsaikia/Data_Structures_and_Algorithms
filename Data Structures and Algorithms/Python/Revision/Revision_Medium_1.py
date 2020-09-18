# ----------------------------------------< Spiral Traverse >-----------------------------------------
# O(mn) Time | O(mn) Space
def spiralTraverse(matrix):
    traversal = []
    startRow, endRow, startCol, endCol = 0, len(
        matrix) - 1, 0, len(matrix[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            traversal.append(matrix[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            traversal.append(matrix[row][endCol])
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                continue
            traversal.append(matrix[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                continue
            traversal.append(matrix[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return traversal


# ----------------------------------------< Longest Peak >-----------------------------------------
# O(N) Time | O(N) Space
def longestPeak(array):
    peaks = getPeaks(array)
    return getLongestPeak(array, peaks)


def getPeaks(array):
    peaks = []
    for idx in range(1, len(array) - 1):
        if array[idx - 1] < array[idx] > array[idx + 1]:
            peaks.append(idx)
    print(peaks)
    return peaks


def getLongestPeak(array, peaks):
    globalLongest = 0

    for peak in peaks:
        startIdx = peak
        while startIdx - 1 >= 0 and array[startIdx - 1] < array[startIdx]:
            startIdx -= 1
        endIdx = peak
        while endIdx + 1 < len(array) and array[endIdx] > array[endIdx + 1]:
            endIdx += 1
        currLongest = endIdx - startIdx
        globalLongest = max(currLongest, globalLongest)
    return globalLongest + 1 if globalLongest != 0 else 0

# ----------------------------------------< Three Sum >-----------------------------------------


'''When the given array has unique integers and required output should be in sorted order'''
# O(n^2) Time | O(n) Space


def threeSum(array, target):
    array.sort()
    triplets = []
    for idx, num in enumerate(array):
        required = target - num
        start = idx + 1
        end = len(array) - 1
        while start < end:
            if array[start] + array[end] == required:
                triplets.append([num, array[start], array[end]])
                start += 1
                end -= 1
            elif array[start] + array[end] > required:
                end -= 1
            else:
                start += 1
    return triplets


'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

IMPORTANT:
Because we need unique triplets, we can do the same sorted approach, but at any moment
duing travering the first loop if we get the current element same as the previous, we skip it
'''
# O(n^2) Time | O(n) Space


def uniqueThreeSum(array, target):
    triplets = set()
    array.sort()
    print(array, "\n\n\n")
    for idx, num in enumerate(array):
        if idx > 0 and array[idx - 1] == num:
            continue
        required = target - num
        start = idx + 1
        end = len(array) - 1
        while start < end:
            if array[start] + array[end] == required:
                triplets.add((num, array[start], array[end]))
                start += 1
                end -= 1
            elif array[start] + array[end] > required:
                end -= 1
            else:
                start += 1
    return [list(triplet) for triplet in triplets]


# ----------------------------------------< Smallest Difference >-----------------------------------------
# O(n log(n) + m log(m)) Time | O(1) Space
def smallestDifference(arrOne, arrTwo):
    arrOne.sort()
    arrTwo.sort()
    elements = []

    globalMin = float("inf")
    arrOneIdx, arrTwoIdx = 0, 0
    while arrOneIdx < len(arrOne) and arrTwoIdx < len(arrTwo):
        currMin = abs(arrOne[arrOneIdx] - arrTwo[arrTwoIdx])
        elementOne = arrOne[arrOneIdx]
        elementTwo = arrTwo[arrTwoIdx]
        if elementOne < elementTwo:
            arrOneIdx += 1
        elif elementOne > elementTwo:
            arrTwoIdx += 1
        else:
            return [arrOneIdx, arrTwoIdx]

        if currMin < globalMin:
            globalMin = currMin
            elements = [elementOne, elementTwo]

    return elements


# ----------------------------------------< Move Elements To End >-----------------------------------------
# O(n) Time | O(1) Space
def moveElementsToEnd(array, num):
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] == num and array[end] != num:
            swap(array, start, end)
        if array[start] != num:
            start += 1
        if array[end] == num:
            end -= 1
    return array


# ----------------------------------------< Monotonic >-----------------------------------------
# O(n) Time | O(1) Space
def isMonotonnic(array):
    return validateMonotonicity(array, "increasing") or validateMonotonicity(array, "indecreasing")


def validateMonotonicity(array, isType):
    for i in range(1, len(array)):
        if compare(array[i - 1], array[i], isType):
            return False
    return True


def compare(num1, num2, isType):
    return num1 > num2 if isType == "increasing" else num1 < num2


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# ----------------------------------------< BST CONSTRUCTION >-----------------------------------------

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(n) Time | O(1) Space
    def printTree(self):
        curr = self
        if curr is None:
            return

        else:
            if curr.left is not None:
                curr.left.printTree()
            if curr.right is not None:
                curr.right.printTree()
        print(curr.value)

    # Average : O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        return self

    # Average : O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def contains(self, value, parent=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False

    # Average : O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def remove(self, value, parent=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.value:
                parent = curr
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.getMinValue()
                    curr.right.remove(curr.value, curr)
                elif parent is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        return None
                elif curr == parent.left:
                    parent.left = curr.left if curr.left is not None else curr.right
                elif curr == parent.right:
                    parent.right = curr.left if curr.left is not None else curr.right
                break
        return self

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value

# ----------------------------------------< Validate BST >-----------------------------------------
# O(n) time || O(log(n)) Space


def validateBST(tree):
    return getValidatedBST(tree, float("-inf"), float("inf"))


def getValidatedBST(node, minValue, maxValue):
    if node is None:
        return True
    if node.value > maxValue or node.value < minValue:
        return False
    return getValidatedBST(node.left, minValue, node.value) and getValidatedBST(node.right, node.value, maxValue)


# ----------------------------------------< Min Height BST >-----------------------------------------
# o(n) Time | O(n) Space
def minHeightBST(array):
    return buildMinHeightBST(array, 0, len(array) - 1)


def buildMinHeightBST(array, startIdx, endIdx):
    if startIdx > endIdx:
        return None

    midIdx = (startIdx + endIdx) // 2
    bst = Node(array[midIdx])
    bst.left = buildMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = buildMinHeightBST(array, midIdx + 1, endIdx)
    return bst

# ----------------------------------------< Invert a Binary Tree >-----------------------------------------
# O(n) Time | O(d) Space


def invertBtRecursive(tree):
    if tree is None:
        return
    invertBtRecursive(tree.left)
    invertBtRecursive(tree.right)
    tree.left, tree.right = tree.right, tree.left

# O(n) Time | O(n) Space


def invertBtIterative(tree):
    que = deque([tree])
    while len(que):
        node = que.popleft()
        if node is None:
            continue
        swap(node)
        que.append(node.left)
        que.append(node.right)


def swap(node):
    node.left, node.right = node.right, node.left


# ----------------------------------------< Maax Subarray Sum No Adjacent >-----------------------------------------
# O(n) Time | O(n) Space
def maxSubarraysum(array):
    if len(array) < 2:
        return array[0] if len(array) == 1 else []
    sums = [0 for _ in array]
    sums[0] = array[0]
    sums[1] = max(array[0], array[1])
    for idx in range(2, len(array)):
        sums[idx] = max(sums[idx - 1], (array[idx] + sums[idx - 2]))
    return sums[-1]

# O(n) Time | O(1) Space


def maxSubarraysumImproved(array):
    if len(array) < 2:
        return array[0] if len(array) == 1 else []

    secondLast, last = array[0], max(array[0], array[1])
    for idx in range(2, len(array)):
        currValue = max(last, (array[idx] + secondLast))
        secondLast, last = last, currValue
    return last


# ----------------------------------------< Num Ways to Make Change >-----------------------------------------
'''
Amount = 10
denoms = [1, 2, 5, 10]

ways    =    [0   1   2   3   4   5   6   7   8   9   10]
denom 1 =    [1   1   1   1   1   1   1   1   1   1   1 ]
denom 2 =    [1   1   2   2   3   3   4   4   5   5   6 ]
denom 5 =    [1   1   2   2   3   4   5   6   6   8   10]
denom 10 =   [1   1   2   2   3   4   5   6   6   8   11]
'''

# O(amount x denom) Time | O(amount) Space


def numberOfWaysToMakeChange(amount, denom):
    ways = [0 for _ in range(amount + 1)]
    ways[0] = 1
    for coin in denom:
        for value in range(1, amount + 1):
            if coin <= value:
                ways[value] += ways[value - coin]
    return ways[-1]


# ----------------------------------------< Min Number Of Coins >-----------------------------------------
# O(amount x denom) Time | O(amount) Space
def minNumberOfCoinsForChange(n, denoms):
    coins = [float('inf') for i in range(n+1)]
    coins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                coins[amount] = min(coins[amount], 1+coins[amount-denom])
    return coins[-1] if coins[-1] != float('inf') else -1


# ----------------------------------------< Levenshtein Distance >-----------------------------------------
# O(mn) Time | O(mn) Space
def editDistance(stringOne, stringTwo):
    edits = [[i for i in range(len(stringTwo) + 1)]
             for row in range(len(stringOne) + 1)]
    for i in range(1, len(edits)):
        edits[i][0] = 1 + edits[i - 1][0]
    for row in range(1, len(edits)):
        for col in range(1, len(edits[0])):
            if stringOne[row - 1] == stringTwo[col - 1]:
                edits[row][col] = edits[row - 1][col - 1]
            else:
                edits[row][col] = 1 + min(edits[row - 1][col],
                                          edits[row][col - 1], edits[row - 1][col - 1])
    return edits[-1][-1]


# ----------------------------------------< Array Single Cycle >-----------------------------------------
# O(n) Time | O(1) Space
def hasSingleCycle(array):
    if len(array) < 2:
        return False
    nextIdx = 0
    for i in range(len(array)):
        if array[nextIdx] != None:
            currIdx = nextIdx
            currVal = array[nextIdx]
            array[nextIdx] = None
            nextIdx = (currIdx+currVal) % len(array)
        else:
            return False

    for each in array:
        if each is not None:
            return False

    return nextIdx == 0


# ----------------------------------------< River Sizes >-----------------------------------------
# O(nm) Time | O(nm) Space
def riverSize(matrix):
    sizes = []
    visited = [[False for col in range(len(matrix[0]))]
               for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]:
                continue
            traverseNode(row, col, matrix, visited, sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currSize = 0
    stack = [[i, j]]
    while len(stack):
        node = stack.pop()
        row, col = node
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        currSize += 1
        children = getNeighbors(row, col, matrix, visited)
        for child in children:
            stack.append(child)
    if currSize > 0:
        sizes.append(currSize)


def getNeighbors(i, j, matrix, visited):
    neighborsX = []
    if i > 0 and not visited[i-1][j]:
        neighborsX.append([i-1, j])
    if i < len(matrix)-1 and not visited[i+1][j]:
        neighborsX.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        neighborsX.append([i, j-1])
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        neighborsX.append([i, j+1])
    return neighborsX


# ----------------------------------------< Yongest common Ancestor >-----------------------------------------
# O(d) Time | O(1) Space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(descendantOne, topAncestor, 0)
    depthTwo = getDepth(descendantTwo, topAncestor, 0)
    if depthOne > depthTwo:
        return getYongest(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return getYongest(descendantTwo, descendantOne, depthTwo - depthOne)


def getDepth(node, root, depth):
    if node is None:
        return depth
    return getDepth(node.ancestor, root, depth + 1)


def getYongest(lower, higher, difference):
    while difference > 0:
        lower = lower.ancestor
        difference -= 1

    while lower != higher:
        lower = lower.ancestor
        higher = higher.ancestor
    return higher


# ----------------------------------------< Min Heap Construction >-----------------------------------------
class Heap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    def peek(self):
        return self.heap[0]
    
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
    
    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        toRemove = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return toRemove
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)
    
    def siftUp(self, array, currentIdx):
        parentIdx = (currentIdx - 1) // 2
        while parentIdx > 0 and array[currentIdx] < array[parentIdx]:
            self.swap(array, parentIdx, currentIdx)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) //2
    
    def siftDown(self, array, currentIdx, endIdx):
        childOneIdx = (2 * currentIdx) + 1
        if childOneIdx <= endIdx:
            childTwoIdx = (childOneIdx + 1) if (childOneIdx + 1) <= endIdx else -1
            if childTwoIdx != -1 and array[childTwoIdx] < array[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if array[currentIdx] > array[idxToSwap]:
                self.swap(array, currentIdx, idxToSwap)
                currentIdx = idxToSwap
                childOneIdx = (2 * currentIdx) + 1
            else:
                return
    
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(array, currentIdx, len(array) - 1)
        return array
        

# ----------------------------------------< Permutations >-----------------------------------------
# O(N^2 . N!) Time | O(N . N!) Space
def permutations(array):
    perms = []
    getPerms(array, [], perms)
    return perms

def getPerms(array, perm, perms):
    if not len(array) and len(perm):
        perms.append(perm)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPerm = perm + [array[i]]
            getPerms(newArray, newPerm, perms)


# O(N. N!) Time | O(N. N!) Space
def getPermutations(array):
    perms = []
    getAllPerms(array, 0, perms)
    return perms

def getAllPerms(array, j, perms):
    if j == len(array):
        perms.append(array[:])
    else:
        for i in range(j, len(array)):
            swapped(array, i, j)
            getAllPerms(array, j + 1, perms)
            swapped(array, i, j)

def swapped(array, i, j):
    array[i], array[j] = array[j], array[i]


# ----------------------------------------< Permutations >-----------------------------------------




if __name__ == "__main__":
    import numpy as np
    from binarytree import Node
    from collections import deque
    from functools import lru_cache

    '''Spiral Traverse'''
    # matrix = [[1, 2, 3, 4],
    #           [12, 13, 14, 5],
    #           [11, 16, 15, 6],
    #           [10, 9, 8, 7]]

    # print(np.array(spiralTraverse(matrix)))

    '''Longest Peak'''
    # array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    # print(longestPeak(array))

    '''Three Sum'''
    # print(threeSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
    # print(uniqueThreeSum([-1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,-1,-4], 0))

    '''Smallest Difference'''
    # arr1 = [-1, 5, 10, 20, 28, 3]
    # arr2 = [26, 134, 135, 15, 17]
    # print(smallestDifference(arr1, arr2))

    '''Move to end'''
    # print(moveElementsToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))

    # print(isMonotonnic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))

    '''BST'''
    # bst = BST(10)
    # bst.insert(30).insert(5).insert(2).insert(12).insert(20)
    # bst.printTree()
    # print(bst.contains(12))
    # bst.remove(12)
    # print("\n")
    # bst.printTree()

    '''Validate BST'''
    # print(validateBST(bst))

    '''Min Height BST'''
    # arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    # bst = minHeightBST(arr)
    # print(bst)

    # invertBtRecursive(bst)
    # print("\n", bst)

    # invertBtIterative(bst)
    # print("\n", bst)

    '''Max Subarray Sum'''
    # array = [75, 105, 120, 75, 90, 135]
    # print(maxSubarraysum(array))
    # print(maxSubarraysumImproved(array))

    '''Make Change'''
    # print(numberOfWaysToMakeChange(10, [1, 2, 5, 10]))
    # print(minNumberOfCoinsForChange(10, [1, 2, 5, 10]))

    '''Edit Distance'''
    # stringOne = "BATD"
    # stringTwo = "ABACD"
    # print(editDistance(stringOne, stringTwo))

    '''Single Cycle Check'''
    # singleCycle = [2, 3, 1, -4, -4, 2]
    # print(hasSingleCycle(singleCycle))

    '''River Sizes'''
    # rivers = [
    #     [1, 0, 0, 1, 0],
    #     [1, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 0, 1, 1, 0]
    # ]
    # print(riverSize(rivers))
    
    '''MinHeap'''
    # arr = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    # heap = Heap(arr)
    # heap.insert(76)
    # print(heap.peek())
    # heap.remove()
    # print(heap.peek())
    # heap.remove()
    # heap.insert(87)
    # print(heap.peek())
    
    '''Perms'''
    # print(permutations([1,2,3]))
    # print(getPermutations([1,2,3]))
    