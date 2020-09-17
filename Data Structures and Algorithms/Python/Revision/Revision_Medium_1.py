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
            


if __name__ == "__main__":
    import numpy as np
    
    '''Spiral Traverse'''
    # matrix = [[1, 2, 3, 4], 
    #           [12, 13, 14, 5], 
    #           [11, 16, 15, 6], 
    #           [10, 9, 8, 7]]
    
    # print(np.array(spiralTraverse(matrix)))
    
    '''Longest Peak'''
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(array))
    
