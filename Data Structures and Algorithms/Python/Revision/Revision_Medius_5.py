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

# print(spiralTraverse(matrix))

arr = [2, 1, 2, 2, 2, 3, 4, 2]
moveElementsToEnd(arr, 2)
print(arr)
