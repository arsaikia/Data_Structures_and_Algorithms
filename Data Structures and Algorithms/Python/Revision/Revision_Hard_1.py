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


if __name__ == "__main__":
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
    from binarytree import Node
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right = Node(3)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    print(tree)
    print(maxPathSum(tree))
