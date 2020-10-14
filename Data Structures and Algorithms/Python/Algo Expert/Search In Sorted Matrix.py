'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    * Integers in each row are sorted from left to right.
    * The first integer of each row is greater than the last integer of the previous row.

matrix = [  [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]    ]
target = 3
Output: true
----------------------------------------------------------------------------------------------------

solution Approach:
1. start at row=0 , col = len(matrix[0]) - 1
2.  If      matrix[row][col] > target: Decrement col
    elif    matrix[row][col] < target: increment col
    else    return True
'''


# O(m + n) Time | O(1) Space
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col > -1:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [1, -1]


if __name__ == "__main__":
    matrix = [[1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]

    target = 23
    print(searchInSortedMatrix(matrix, target))
