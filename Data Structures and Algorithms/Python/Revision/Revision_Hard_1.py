# ----------------------------------------< Four Number Sum >-----------------------------------------------
'''
Time Complexity Analysis:
Average: O(n^2) Time    |   O(n^2) Space
        For each value in outer for loop we have two inner forloops which 
        takes n^2 Time each => O(2 n^2) => O(n^2)

Worst:  O(n^3)  |   O(N^2) Space
        In a really worse case where we have values like [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        and target 0, we will have a lot of children in complement hashtable for sum 0 : 
        [ [-1, 1], [-2, 2], [-3, 3], [-4, 4]]
        In such scenarios, the time to traverse through the children will also come into 
        picture making the time complexity more in O(n^3) than O(n^2)
        IN MOST CASES IT WILL BE O(n^2)
  
In both cases we are storing n^2 values in the hashtable, which causes this space complexity.      
'''


import heapq as heap


def fourSum(array, target):
    complements = {}
    allSums = []
    for i in range(1, len(array) - 1):
        for j in range(i, len(array)):
            required = target - (array[i] + array[j])
            if required in complements:
                for sums in complements[required]:
                    allSums.append([sums + [array[i], array[j]]])
        for k in range(0, i + 1):
            if array[i] + array[k] not in complements:
                complements[array[i] + array[k]
                            ] = [sorted([array[i], array[k]])]
            else:
                complements[array[i] + array[k]
                            ].append(sorted([array[i], array[k]]))

    return allSums


# ----------------------------------------< Subarray Sort >-----------------------------------------------
# O(n) Time | O(1) Space
def subarraysort(array):
    minOutOfPlace = float("inf")
    maxOutOfPlace = float("-inf")

    for idx, num in enumerate(array):
        if isOutOfPlace(array, num, idx):
            minOutOfPlace = min(minOutOfPlace, num)
            maxOutOfPlace = max(maxOutOfPlace, num)

    start, end = 0, len(array) - 1
    while start < len(array):
        if minOutOfPlace > array[start]:
            start += 1
        else:
            break
    while end > -1:
        if maxOutOfPlace < array[end]:
            end -= 1
        else:
            break

    print(start, end)


def isOutOfPlace(array, num, idx):
    if idx == 0:
        return num > array[idx + 1]
    if idx == len(array) - 1:
        return array[idx] < array[len(array) - 2]

    return array[idx - 1] > array[idx] or array[idx + 1] < array[idx]


# ----------------------------------------< Largest Range >-----------------------------------------------
# O(n) Time | O(n) Space
def largestRange(array):
    nums = {num: True for num in array}
    longest = []
    globalMax = float("-inf")

    for each in array:
        if each in nums:
            currMax = 1
            left = each - 1
            while left in nums:
                left -= 1
                currMax += 1
            right = each + 1
            while right in nums:
                right += 1
                currMax += 1
            if currMax > globalMax:
                globalMax = currMax
                longest = [left + 1, right - 1]
    return longest


# ----------------------------------------< Largest Range >-----------------------------------------------
# O(n) Time | O(1) Space
def minRewards(array):
    rewards = [1 for _ in array]
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(array) - 1)):
        if array[i] > array[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return rewards


# ----------------------------------------< Zigzag Traverse >-----------------------------------------------
# O(nm) Time | O(nm) Space
def zigzagTrverse(array):
    result = []
    startRow, startCol, endRow, endCol = 0, 0, len(
        array) - 1, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                continue
            result.append(array[row][col])
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                continue
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


# ----------------------------------------< SAME BSTS >-----------------------------------------------
# O(n) Time | O(d) Space where d is the depth of the BST
def sameBst(arr1, arr2):

    if len(arr1) == 0:
        return True

    if len(arr1) != len(arr2):
        return False

    if arr1[0] != arr2[0]:
        return False

    leftOne, rightOne = getLeftAndRight(arr1)
    leftTwo, rightTwo = getLeftAndRight(arr2)

    return sameBst(leftOne, leftTwo) and sameBst(rightOne, rightTwo)


def getLeftAndRight(array):
    left = [array[i] for i in range(1, len(array)) if array[i] < array[0]]
    right = [array[i] for i in range(1, len(array)) if array[i] >= array[0]]
    return left, right


# ----------------------------------------< Max Path sum in BT >-----------------------------------------------
# O(n) Time | O(log n) Space
def maxPathSum(tree):
    _, maxPathSum = getMaxPathSum(tree)
    return maxPathSum


def getMaxPathSum(node):
    if node is None:
        return 0, float("-inf")

    LCBS, LPS = getMaxPathSum(node.left)
    RCBS, RPS = getMaxPathSum(node.right)
    childSum = max(LCBS, RCBS)
    branchSum = max(node.value, childSum + node.value)
    pathSum = max(LPS, RPS, branchSum, LCBS + node.value + RCBS)

    return branchSum, pathSum


# ----------------------------------------< Max Sum Increasing Subsequence >-----------------------------------------------
# O(n^2) Time | O(n) Space
def maxIncreasingSum(array):
    sums = array[:]
    maxSumIdx = 0
    sequence = [None for _ in array]

    for i in range(1, len(array)):
        currNum = array[i]
        for j in range(0, i):
            prevNum = array[j]
            if prevNum < currNum and sums[j] + array[i] > sums[i]:
                sums[i] = sums[j] + array[i]
                sequence[i] = j
        if sums[i] > sums[maxSumIdx]:
            maxSumIdx = i
    return buildSequence(array, sequence, maxSumIdx)


def buildSequence(array, sequence, maxSumIdx):
    seq = []

    while maxSumIdx is not None:
        seq.append(array[maxSumIdx])
        maxSumIdx = sequence[maxSumIdx]
    return list(reversed(seq))

# ----------------------------------------< LCS >--------------------------------------------------------------------------
# O(2^(m+n) Time)


def recusiveLCS(stringOne, stringTwo):
    return getLCS(stringOne, stringTwo, len(stringOne) - 1, len(stringTwo) - 1)


def getLCS(s1, s2, m, n):
    if m < 0 or n < 0:
        return 0

    count = 0

    if s1[m] == s2[n]:
        count = 1 + getLCS(s1, s2, m - 1, n - 1)
    else:
        count = max(getLCS(s1, s2, m - 1, n), getLCS(s1, s2, m, n - 1))
    return count

# ----------------------------------------< LCS MEMOIZED


def memoizedLCS(stringOne, stringTwo):

    def trverseSubstring(string, memo):
        sequence = []
        row = len(memo) - 1
        col = len(memo[0]) - 1
        while row > 0 and col > 0:
            if memo[row][col] == memo[row - 1][col]:
                row -= 1
            elif memo[row][col] == memo[row][col - 1]:
                col -= 1
            else:
                sequence.append(string[row - 1])
                row -= 1
                col -= 1
        return "".join(list(reversed(sequence)))

    def memoizedLCSX(stringOne, stringTwo):
        memo = [[0 for col in stringTwo] for row in stringOne]
        getMemoizedLCS(stringOne, stringTwo, len(
            stringOne) - 1, len(stringTwo) - 1, memo)
        print(trverseSubstring("BATD", memo))
        print(np.array(memo))

    def getMemoizedLCS(s1, s2, m, n, memo):
        if m < 0 or n < 0:
            return 0

        if memo[m][n]:
            return memo[m][n]

        count = 0

        if s1[m] == s2[n]:
            count = 1 + getMemoizedLCS(s1, s2, m - 1, n - 1, memo)
        else:
            count = max(getMemoizedLCS(s1, s2, m - 1, n, memo),
                        getMemoizedLCS(s1, s2, m, n - 1, memo))

        memo[m][n] = count
        return count

    return memoizedLCSX(stringOne, stringTwo)

# ----------------------------------------< LCS BOTTOMS UP
# O(mn) Time | O(mn) Space


def bottomupLcs(s1, s2):
    cache = [[0 for col in range(len(s1) + 1)] for row in range(len(s2) + 1)]
    for row in range(1, len(cache)):
        for col in range(1, len(cache[0])):
            if s1[col - 1] == s2[row - 1]:
                cache[row][col] = 1 + cache[row - 1][col - 1]
            else:
                cache[row][col] = max(cache[row - 1][col], cache[row][col - 1])

    print("\n", np.array(cache))
    return (getCommonSubstring(stringOne, cache))


def getCommonSubstring(string, cache):
    row = len(cache) - 1
    col = len(cache[0]) - 1
    substring = []
    while row > 0 and col > 0:

        if cache[row][col] == cache[row - 1][col]:
            row -= 1
        elif cache[row][col] == cache[row][col - 1]:
            col -= 1
        else:
            substring.append(string[col - 1])
            row -= 1
            col -= 1
    return "".join(list(reversed(substring)))


# ----------------------------------------< Min Num Of Jumps >--------------------------------------------------------------
def minNumOfJumps(array):
    jumps = [float("inf") for _ in array]
    jumps[0] = 0

    for i in range(1, len(jumps)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]


# ----------------------------------------< Water Area >--------------------------------------------------------------
# O(n) Time | O(n) Space
def waterArea(array):
    leftMax = [0 for _ in array]
    rightMax = [0 for _ in array]
    leftM = 0
    rightM = 0
    area = [0 for _ in array]

    for i in range(len(array)):
        leftMax[i] = max(leftM, array[i])
        leftM = max(leftM, array[i])
    for i in reversed(range(len(array))):
        rightMax[i] = max(rightM, array[i])
        rightM = max(rightM, array[i])

    for i in range(len(array)):
        left = leftMax[i]
        right = rightMax[i]
        curr = array[i]
        height = min(left, right)
        if height > curr:
            area[i] = height - curr
    return sum(area)


# ----------------------------------------< 0-1 Knapsack >--------------------------------------------------------------
# O(nm) Time | O(nm) Space
def knapsack(items, capacity):
    knapsackMatrix = [[0 for i in range(capacity + 1)]
                      for j in range(len(items) + 1)]
    for item in range(1, len(items) + 1):
        currValue = items[item - 1][0]
        currWeight = items[item - 1][1]
        for weightCapacity in range(1, capacity + 1):
            if currWeight > weightCapacity:
                knapsackMatrix[item][weightCapacity] = knapsackMatrix[item -
                                                                      1][weightCapacity]
            else:
                knapsackMatrix[item][weightCapacity] = max(
                    knapsackMatrix[item - 1][weightCapacity], currValue + knapsackMatrix[item - 1][weightCapacity - currWeight])

    return getItemsInKnapsack(knapsackMatrix, items)


def getItemsInKnapsack(matrix, items):
    seq = []
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    while row > 0:
        if matrix[row][col] == matrix[row - 1][col]:
            row -= 1
        else:
            seq.append(items[row - 1])
            col = col - items[row - 1][1]
            row -= 1
    return list(reversed(seq))


# ----------------------------------------< Disk Stacking >--------------------------------------------------------------
# O(n^2) Time | O(n) Space
def stackDisks(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequence = [None for _ in disks]
    maxHeightIdx = 0

    for i in range(1, len(heights)):
        currDisk = disks[i]
        for j in range(0, i):
            prevDisk = disks[j]
            if canGoOnTop(prevDisk, currDisk):
                if heights[j] + currDisk[2] > heights[i]:
                    heights[i] = heights[j] + currDisk[2]
                    sequence[i] = j
        if heights[i] > heights[maxHeightIdx]:
            maxHeightIdx = i
    return buildHeightSequence(sequence, maxHeightIdx, disks)


def canGoOnTop(prev, curr):
    return prev[0] < curr[0] and prev[1] < curr[1] and prev[2] < curr[2]


def buildHeightSequence(sequence, maxHeightIdx, disks):
    seq = []
    while maxHeightIdx is not None:
        seq.append(disks[maxHeightIdx])
        maxHeightIdx = sequence[maxHeightIdx]
    return list(reversed(seq))


# ----------------------------------------< Numbers In PI >--------------------------------------------------------------
# TOP-DOWN
# O(n^3 + m) Space | O(n + m) Space
def minSpacesForNumbersInPi(pi, numbers):
    allNums = {num: True for num in numbers}
    cache = {}
    minSpaces = getMinSpacesStartingAtIdx(pi, allNums, 0, cache)
    return minSpaces


def minSpacesForNumbersInPiBottomUp(pi, numbers):
    allNums = {num: True for num in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpacesStartingAtIdx(pi, allNums, i, cache)
    return cache[0]

# Bottom-up
# O(n^3 + m) Space | O(n + m) Space


def getMinSpacesStartingAtIdx(pi, nums, idx, cache):
    if idx == len(pi):
        return 0
    if idx in cache:
        return cache[idx]

    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in nums:
            currSpaces = 1 + getMinSpacesStartingAtIdx(pi, nums, i + 1, cache)
            minSpaces = min(minSpaces, currSpaces)
    cache[idx] = minSpaces
    return minSpaces


# ----------------------------------------< Contiuous Median >--------------------------------------------------------------

class ContinuousMedianHandler:
    def __init__(self):
        self.lowerHalf = []     # MAX HEAP
        self.upperHalf = []     # MIN HEAP
        self.median = None
    # O(log n) Time | O(n) Space

    def insert(self, number):
        if not len(self.lowerHalf) or number < (-1 * self.lowerHalf[0]):
            heap.heappush(self.lowerHalf, -1 * number)
        else:
            heap.heappush(self.upperHalf, number)
        self.rebalanceHeaps()
        self.calculateMedian()

    def rebalanceHeaps(self):
        if len(self.lowerHalf) - len(self.upperHalf) == 2:
            heap.heappush(self.upperHalf, -1 * heap.heappop(self.lowerHalf))
        elif len(self.upperHalf) - len(self.lowerHalf) == 2:
            heap.heappush(self.lowerHalf, -1 * heap.heappop(self.upperHalf))

    def calculateMedian(self):
        if len(self.lowerHalf) == len(self.upperHalf):
            self.median = ((self.lowerHalf[0] * -1) + self.upperHalf[0]) / 2
        elif len(self.lowerHalf) > len(self.upperHalf):
            self.median = self.lowerHalf[0] * -1
        else:
            self.median = self.upperHalf[0]

    def getMedian(self):
        return self.median



# ----------------------------------------< Find Loop in a Singly Linked List >--------------------------------------------------------------
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space
def findLoop(head):
    slowPtr = head.next
    fastPtr = head.next.next
    
    while slowPtr != fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
    
    slowPtr = head
    
    while slowPtr != fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next
    
    return slowPtr
 
# ----------------------------------------< Reverse a Singly Linked List >--------------------------------------------------------------
# O(n) Time | O(1) Space
def reverseLinkedList(head):
    p1, p2 = None, head
    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1



# ------------------------------------------------< MAIN >------------------------------------------------------------------
if __name__ == "__main__":
    # from functools import lru_cache
    import numpy as np

    '''Four Number Sum'''
    # array = [7, 6, 4, -1, 1, 2]
    # target = 16
    # print(fourSum(array, target))

    '''Subarray Sort'''
    # array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    # print(subarraysort(array))

    '''Largest Range'''
    # array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    # print(largestRange(array))

    '''Min Rewards'''
    # rewards = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    # print(minRewards(rewards))

    '''Zigzag Traverse'''
    # array = [[1, 2, 3, 4],
    #          [12, 13, 14, 5],
    #          [11, 16, 15, 6],
    #          [10, 9, 8, 7]]
    # print(zigzagTrverse(array))

    '''Same Bsts'''
    # arrayOne = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    # arrayTwo = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    # print(sameBst(arrayOne, arrayTwo))

    '''maxPathSum'''
    # from binarytree import Node
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.left.left = Node(4)
    # tree.left.right = Node(5)
    # tree.right = Node(3)
    # tree.right.left = Node(6)
    # tree.right.right = Node(7)
    # print(tree)
    # print(maxPathSum(tree))

    '''Max Sum Increasing Subsequence'''
    # array = [10, 70, 20, 30, 50, 11, 30]
    # print(maxIncreasingSum(array))

    '''LCS'''
    # stringOne = "BATD"
    # stringTwo = "ABACD"
    # import time
    # one = time.perf_counter()
    # print("recusiveLCS", recusiveLCS(stringOne, stringTwo))
    # two = time.perf_counter()
    # print(two - one)
    # print("memoizedLCS", memoizedLCS(stringOne, stringTwo))
    # three = time.perf_counter()
    # print(three - two)
    # print(bottomupLcs(stringOne, stringTwo))

    '''Jums Game'''
    # jumps = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    # print(minNumOfJumps(jumps))

    '''Water Area'''
    # water = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    # print(waterArea(water))

    ''''knapsack'''
    # items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    # capacity = 10
    # print(knapsack(items, capacity))

    '''Stack Disks'''
    # disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    # print(stackDisks(disks))

    '''Numbers in Pi'''
    # pi = "3141592653589793238462643383279"
    # numbers = [
    #     "314159265358979323846",
    #     "26433",
    #     "8",
    #     "3279",
    #     "314159265",
    #     "35897932384626433832",
    #     "79"
    # ]

    # print(minSpacesForNumbersInPi(pi, numbers))
    # print(minSpacesForNumbersInPiBottomUp(pi, numbers))

    '''Contiuous Median'''
    # median = ContinuousMedianHandler()
    # median.insert(1)
    # median.insert(10)
    # median.insert(20)
    # median.insert(30)
    # median.insert(40)
    # median.insert(50)
    # print(median.lowerHalf, median.upperHalf, median.getMedian())
    
    '''' Linked List Loop'''
    llist = LinkedList(1)
    llist.next = LinkedList(2)
    llist.next.next = LinkedList(3)
    loop = llist.next.next.next = LinkedList(4)
    loop.next = LinkedList(5)
    loop.next.next = LinkedList(6)
    loop.next.next.next = LinkedList(7)
    loop.next.next.next.next = LinkedList(8)
    x = loop.next.next.next.next.next = LinkedList(9)
    x.next = loop
    
    nodeWithLoop = findLoop(llist)
    print(nodeWithLoop.value)
    
    '''Reverse LinkedList'''
    revLlist = reverseLinkedList(llist)
    print(revLlist.value)