'''
Rotate Image: Clockwise
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose
[
    [1, 4, 7],
    [2, 5, 8],
    [7, 6, 9]
]

# Reverse Rows
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
'''


def rotateClockwise(matrix):
    # Transpose
    for row in range(len(matrix)):
        for col in range(row, len(matrix[0])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # Inverse Rows
    for row in matrix:
        row.reverse()

    return matrix


def rotateAnticlockwise( matrix ):
    # Inverse Rows
    for row in matrix:
        row.reverse()
    
    # Transpose
    for row in range(len(matrix)):
        for col in range(row, len(matrix[0])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    return matrix


if __name__ == "__main__":
    import numpy as np
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(np.array(rotateAnticlockwise(matrix)))
