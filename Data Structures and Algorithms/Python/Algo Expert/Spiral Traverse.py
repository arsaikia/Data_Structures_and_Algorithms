import numpy as np

'''

Spiral Matrix:
    
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

'''


def spiralTraverse(matrix):
    startRow, endRow = 0, len(matrix) - 1
    startCol, endCol = 0, len(matrix[0]) - 1
    result = []
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(matrix[startRow][col])
        
        for row in range(startRow + 1, endRow + 1):
            result.append(matrix[row][endCol])
        
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow: continue
            result.append(matrix[endRow][col])
        
        for row in reversed(range(startRow - 1, endRow)):
            if startCol == endCol: continue
            result.append(matrix[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result
    


if __name__ == "__main__":
    matrix = np.array([
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ])
    print(spiralTraverse(matrix))
