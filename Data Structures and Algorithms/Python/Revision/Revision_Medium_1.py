# ----------------------------------------< Spiral Traverse >-----------------------------------------
# O(mn) Time | O(mn) Space
def spiralTraverse(matrix):
    traversal = []
    startRow, endRow, startCol, endCol = 0,len(
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
        currLongest =  endIdx - startIdx
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
    arr1 = [-1, 5, 10, 20, 28, 3]
    arr2 = [26, 134, 135, 15, 17]
    print(smallestDifference(arr1, arr2))
    
    
