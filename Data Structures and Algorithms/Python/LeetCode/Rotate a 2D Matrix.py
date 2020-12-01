from typing import List

def rotateMatrix( matrix: List[List[int]] ):
    # Step 1: Transpose
    for rowIdx, row in enumerate(matrix):
        for colIdx in range(rowIdx, len(matrix[0])):
            matrix[rowIdx][colIdx], matrix[colIdx][rowIdx] = matrix[colIdx][rowIdx], matrix[rowIdx][colIdx]
    
    

    # Step 2: reverse each row
    for row in matrix:
        row.reverse()

    print(matrix)
    
    






if __name__ == "__main__":
    matrix : List[List[int]] = [    [1,2,3],
                                    [4,5,6],
                                    [7,8,9]     ]

    rotateMatrix(matrix)