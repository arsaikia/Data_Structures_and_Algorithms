class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # hash-maps to store values seen so far
        visitedRows = collections.defaultdict(set)    # { rowIDx : set( values ) }
        visitedCols = collections.defaultdict(set)    # { colIdx: set( values ) }
        visitedGrids = collections.defaultdict(set)   # { (rowIdx // 3, colIdx // 3) : set(vales)}

        for row in range(ROWS):
            for col in range(COLS):
                value = board[row][col]

                if value == ".":
                    continue

                # check if val is already in current row
                if value in visitedRows[row]:
                    return False
                
                # check if value is already in current col
                if value in visitedCols[col]:
                    return False
                
                # check if value is already in current 3 x 3 grid
                if value in visitedGrids[ (row // 3, col // 3) ]:
                    return False
                
                # add value to visited hash-maps
                visitedRows[row].add(value)
                visitedCols[col].add(value)
                visitedGrids[( row // 3, col // 3 )].add(value)

        return True
        