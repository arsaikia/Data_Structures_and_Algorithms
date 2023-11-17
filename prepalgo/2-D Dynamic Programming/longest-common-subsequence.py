# BOTTOM-UP
# O(m*n) Time | O(m*n) Space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        cache = [ [0 for col in range(COLS + 1)] for row in range(ROWS + 1) ]

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                charOne, charTwo = text1[row], text2[col]
                if charOne == charTwo:
                    cache[row][col] = 1 + cache[row + 1][col + 1]
                else:
                    cache[row][col] = max(cache[row + 1][col], cache[row][col + 1])
        
        return cache[0][0]
    

#####################################################################################
# TOP-DOWN with Memoization/Cache
# TLE
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        cache = [ [0 for col in range(COLS)] for row in range(ROWS) ]
        cache[-1][-1] = 1

        def traverse(row, col):

            # Negative Base Case
            if row == ROWS or col == COLS:
                return 0
            
            # Found Cache
            if cache[row][col] > 1:
                return cache[row][col]
            
            charOne, charTwo = text1[row], text2[col]
            if charOne == charTwo:
                cache[row][col] = 1 + traverse(row + 1, col + 1)
            else:
                cache[row][col] = max(traverse(row + 1, col), traverse(row, col + 1))
            
            return cache[row][col]
        
        return traverse(0, 0)

