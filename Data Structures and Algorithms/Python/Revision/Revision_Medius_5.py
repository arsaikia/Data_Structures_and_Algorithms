import re
import collections


def spiralTraverse(matrix):
    rowStartIdx, rowEndIdx = 0, len(matrix) - 1
    colStartIdx, colEndIdx = 0, len(matrix[0]) - 1
    results = []

    while rowStartIdx <= rowEndIdx and colStartIdx <= colEndIdx:
        for col in range(colStartIdx, colEndIdx + 1):
            results.append(matrix[rowStartIdx][col])

        for row in range(rowStartIdx + 1, rowEndIdx + 1):
            results.append(matrix[row][colEndIdx])

        for col in reversed(range(colStartIdx, colEndIdx)):
            if rowStartIdx == rowEndIdx:
                continue
            results.append(matrix[rowEndIdx][col])

        for row in reversed(range(rowStartIdx + 1, rowEndIdx)):
            if colStartIdx == colEndIdx:
                continue
            results.append(matrix[row][colStartIdx])

        rowStartIdx += 1
        rowEndIdx -= 1
        colStartIdx += 1
        colEndIdx -= 1

    return results

# [4, 1, 3, 2, 2, 2, 2, 2]


def moveElementsToEnd(arr, elementToMove):
    startIdx, endIdx = 0, len(arr) - 1
    while startIdx < endIdx:
        left = arr[startIdx]
        right = arr[endIdx]

        if left == elementToMove and right != elementToMove:
            arr[startIdx], arr[endIdx] = arr[endIdx], arr[startIdx]

        if left != elementToMove:
            startIdx += 1

        if right == elementToMove:
            endIdx -= 1


matrix = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]
          ]


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    return
                curr = curr.left
            else:
                if value > curr.value:
                    if curr.right is None:
                        curr.right = BST(value)
                        return
                    curr = curr.right


def minBst(arr, i, j):
    if i > j:
        return None
    mid = (i + j) // 2
    node = BST(arr[mid])
    node.left = minBst(arr, i, mid - 1)
    node.right = minBst(arr, mid + 1, j)

    return node


# O(m x n) Time | O(m x n) Space
def levenshteinDistance(str1, str2):
    edits = [[i for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for row in range(1, len(edits)):
        edits[row][0] += edits[row - 1][0]

    for row in range(1, len(str2) + 1):
        for col in range(2, len(str1) + 1):
            firstStringLetter = str1[col - 1]
            secondStringLetter = str2[row - 1]
            if firstStringLetter == secondStringLetter:
                edits[row][col] = edits[row - 1][col - 1]
            else:
                edits[row][col] = 1 + (min(edits[row - 1][col - 1],
                                           edits[row - 1][col], edits[row][col - 1]))

    return edits[-1][-1]


def riverSizes(matrix):
    sizes = []
    visited = [[False for col in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]:
                continue
            traverseNode(row, col, matrix, visited, sizes)

    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currSize = 0
    nodes = [[i, j]]

    while len(nodes):
        node = nodes.pop()
        row = node[0]
        col = node[1]
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        currSize += 1
        neighbors = getNeighbors(row, col, matrix, visited)
        for neighbor in neighbors:
            nodes.append(neighbor)

    if currSize > 0:
        sizes.append(currSize)


def getNeighbors(row, col, matrix, visited):
    neighbors = []
    if row > 0 and not visited[row - 1][col]:
        neighbors.append([row - 1, col])
    if row < len(matrix) - 1 and not visited[row + 1][col]:
        neighbors.append([row + 1, col])
    if col > 0 and not visited[row][col - 1]:
        neighbors.append([row, col - 1])
    if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
        neighbors.append([row, col + 1])
    return neighbors


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)

    def siftUp(self, arr, currIdx):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and arr[currIdx] < arr[parentIdx]:
            self.swap(self.heap, currIdx, parentIdx)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        toRemove = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return toRemove

    def siftDown(self, arr, currentIdx, endIdx):
        childOneIdx = (2 * currentIdx) + 1
        while childOneIdx <= endIdx:
            childTwoIdx = childOneIdx + 1 if childOneIdx + 1 <= endIdx else -1
            if childTwoIdx != -1 and arr[childTwoIdx] < arr[childOneIdx]:
                minIdxToSwap = childTwoIdx
            else:
                minIdxToSwap = childOneIdx

            if arr[currentIdx] < arr[childOneIdx]:
                self.swap(currentIdx, minIdxToSwap)
                currentIdx = minIdxToSwap
                childOneIdx = (2 * currentIdx) + 1
            else:
                return

    def buildHeap(self, arr):
        firstParentIdx = (len(arr) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(arr, currentIdx, len(arr) - 1)
        return arr

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


def longestPalindrome(string):
    longest = [0, 1]
    for i in range(1, len(string)):
        odd = getPalindrome(string, i - 1, i + 1)
        even = getPalindrome(string, i - 1, i)
        currLongest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(currLongest, longest, key=lambda x: x[1] - x[0])
    return string[longest[0]: longest[1]]


def getPalindrome(string, left, right):
    while left >= 0 and right <= len(string) - 1:
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left + 1, right]


# print(spiralTraverse(matrix))
arr = [2, 1, 2, 2, 2, 3, 4, 2]
# moveElementsToEnd(arr, 2)
# print(arr)
# print(levenshteinDistance('abc', 'yabd'))

rivers = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]


# print(riverSizes(rivers))

# print(longestPalindrome("abaxyzzyxf"))


def minWindowSubstring(string, sub):
    charCounts = collections.Counter(sub)
    subBound = getBounds(string, sub, charCounts)
    if subBound[1] == float('inf'):
        return ""
    return string[subBound[0]: subBound[1] + 1]


def getBounds(s, ss, charCounts):
    bounds = [0, float('inf')]
    subCharCounts = {}
    uniqueNeeded = len(charCounts)
    uniqueFound = 0

    left, right = 0, 0
    while right < len(s):
        rightChar = s[right]
        if rightChar not in charCounts:
            right += 1
            continue
        subCharCounts[rightChar] = subCharCounts.get(rightChar, 0) + 1
        if subCharCounts[rightChar] == charCounts[rightChar]:
            uniqueFound += 1

        while uniqueFound == uniqueNeeded and left <= right:
            bounds = [left, right] if right - \
                left < bounds[1] - bounds[0] else bounds
            leftChar = s[left]
            if leftChar not in charCounts:
                left += 1
                continue
            if subCharCounts[leftChar] == charCounts[leftChar]:
                uniqueFound -= 1
            if leftChar in subCharCounts:
                subCharCounts[leftChar] -= 1
            left += 1
        right += 1
    return bounds


# print(minWindowSubstring("ADOBECODEBANC", "ABC"))


def firstUnique(string):
    allChars = {}
    for ch in string:
        if ch not in allChars:
            allChars[ch] = 1
        else:
            allChars[ch] += 1
    for idx, ch in enumerate(string):
        if allChars[ch] == 1:
            return idx, ch


# print(firstUnique('leetcode'))

pattern = '^a....s$'
test_string = 'apples'
# print(re.match(pattern, test_string))

pattern = '[abc]'
# print('abcabc'.split('b', 1))


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

Output = ["let1 art can", "let3 art zero",
          "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]


def orderLog(logs):
    letterLogs = []
    digitLogs = []
    for log in logs:
        parts = log.split(" ", 1)
        if parts[1][0].isdigit():
            digitLogs.append(log)
        else:
            letterLogs.append(log)

    letterLogs.sort(key=lambda x: (x.split(" ")[1], x.split(" ")[0]))
    letterLogs.extend(digitLogs)
    return letterLogs


# print(orderLog(logs) == Output)

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def quickselect(arr, i, j, pos):

    while True:
        if i > j:
            return
        start = i
        pivot = start + 1
        end = j
        while start < end:
            startEl = arr[start]
            endEl = arr[end]
            pivotEl = arr[pivot]
            print(arr, startEl, endEl, pivotEl)
            if startEl > pivotEl and endEl < pivotEl:
                swap(arr, start, end)
            if startEl <= pivotEl:
                start += 1
            if endEl >= pivotEl:
                end -= 1
        swap(arr, pivot, end)
        if end == pos:
            return arr[pos]
        elif pos < end:
            j = end - 1
        else:
            i = end + 1


arr = [3, 2, 1, 5, 6, 4]
# print(quickselect(arr, 0, len(arr) - 1, len(arr) - 2))


#   Longest Substring Without Repeating Characters

s = "abcabcbb"


def longestSubstring(string):
    visited = {}
    startIdx = 0
    longest = 0

    for idx, ch in enumerate(string):
        if ch not in visited:
            visited[ch] = idx
        else:
            startIdx = max(startIdx, visited[ch] + 1)
            visited[ch] = idx
        longest = max(longest, idx - startIdx + 1)
    return longest


# print(longestSubstring(s))

# String to Integer (atoi)
'''
+123Words
-1232asdas
12321dsfds
sadasd1232
'''


def strToInt(string):
    string = string.strip()
    val = set([str(i) for i in range(10)])

    if not len(string):
        return 0

    isPositive = True
    if string[0] == '+' or string[0] == '-':
        isPositive = string[0] == '+'
        string = string[1:]

    number = getDigits(string, val)
    return signedInt(number, isPositive)


def getDigits(s, digits):
    result = []
    for ch in s:
        if ch in digits:
            result.append(ch)
        else:
            break
    return int("".join(result)) if len(result) else 0


def signedInt(number, isPositive):
    if not isPositive:
        number = -1 * number

    if isPositive and number > pow(2, 31) - 1:
        return pow(2, 31) - 1
    elif number < pow(2, 31) * - 1:
        return pow(2, 31) * - 1
    return number


# print(strToInt('ww1x23213  w'))


def containerWithMostWater(height):
    startIdx = 0
    endIdx = 8

    area = 0

    while startIdx < endIdx:
        left = height[startIdx]
        right = height[endIdx]
        currHeight = min(height[startIdx], height[endIdx])
        width = endIdx - startIdx
        area = max(area, currHeight * width)

        if left < right:
            startIdx += 1
        else:
            endIdx -= 1

    return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(containerWithMostWater(height))

string = "aefoaefcdaefcdaed"
substring = "aefcdaed"


def findPattern(s, ss):
    if len(substring) > len(string):
        return False

    pattern = getPattern(ss)
    return doesMatch(s, ss, pattern)


def getPattern(ss):
    pattern = [-1 for _ in range(len(ss))]
    j, i = 0, 1

    while i < len(ss):
        if ss[i] == ss[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


def doesMatch(s, ss, pattern):
    j, i = 0, 0

    while i < len(s):
        if s[i] == ss[j]:
            if j == len(ss) - 1:
                return i - (len(ss) - 1)
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return -1


# print(findPattern(string, substring))


# Minimum Window Substring
from collections import  Counter
def minWindow(s, ss):
    charCounts = Counter(ss)
    bounds = getBounds(s, charCounts)
    if bounds[1] == float('inf'):
        return ""
    return s[bounds[0] : bounds[1] + 1]

def getBounds(s, charCounts):
    bounds = [0, float('inf')]
    leftIdx, rightIdx = 0, 0
    visited = {}
    uniqueNeeded = len(charCounts)
    uniqueFound = 0

    while rightIdx < len(s):
        rightChar = s[rightIdx]
        if rightChar not in charCounts:
            rightIdx += 1
            continue
        visited[rightChar] = visited.get(rightChar, 0) + 1
        if visited[rightChar] == charCounts[rightChar]:
            uniqueFound += 1
        
        while uniqueFound == uniqueNeeded and leftIdx <= rightIdx:
            bounds = min(bounds, [leftIdx, rightIdx], key = lambda x : x[1] - x[0] )
            leftChar = s[leftIdx]
            if leftChar not in charCounts:
                leftIdx += 1
                continue
            if visited[leftChar] == charCounts[leftChar]:
                uniqueFound -= 1
            if leftChar in visited:
                visited[leftChar] -= 1
            leftIdx += 1
        
        rightIdx += 1

    return bounds



s = "ADOBECODEBANC"
ss = "ABC"

print(minWindow(s, ss))