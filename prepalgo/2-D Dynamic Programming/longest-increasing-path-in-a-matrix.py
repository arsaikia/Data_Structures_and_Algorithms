# O(MxN) Time | O(MxN) Space
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [ [0 for col in row] for row in matrix ]

        def dfs(row, col, prevVal):
            if row not in range(ROWS) or col not in range(COLS) or matrix[row][col] <= prevVal:
                return 0
            if cache[row][col]:
                return cache[row][col]
            
            path = 1

            path = max(path, 1 + dfs(row + 1, col, matrix[row][col]))
            path = max(path, 1 + dfs(row, col + 1, matrix[row][col]))
            path = max(path, 1 + dfs(row - 1, col, matrix[row][col]))
            path = max(path, 1 + dfs(row, col -1, matrix[row][col]))
    
            cache[row][col] = path
            return cache[row][col]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        maxVal = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxVal = max(cache[r][c], maxVal)
        return maxVal
