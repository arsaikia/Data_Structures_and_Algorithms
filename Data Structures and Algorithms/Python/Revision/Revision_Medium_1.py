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


if __name__ == "__main__":
    import numpy as np

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

    bst = BST(10)
    bst.insert(30).insert(5).insert(2).insert(12).insert(20)
    bst.printTree()
    print(bst.contains(12))
    bst.remove(12)
    print("\n")
    bst.printTree()
