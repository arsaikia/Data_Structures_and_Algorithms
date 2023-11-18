# Bottom Up
# O(m x n) Time | O(m x n) Space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [ [float("inf") for __ in range(len(word1) + 1)] for __ in range(len(word2) + 1) ]

        # fill up bottom row in 2D cache
        for col in range(len(cache[0])):
            row = len(cache) - 1
            cache[row][col] = (len(cache[0])- 1) - col

        # fill up right col in 2D cache
        for row in range(len(cache)):
            col = len(cache[0]) - 1
            cache[row][col] = (len(cache) - 1) - row
        
        # traverse cache and fill up bottom up
        for row in reversed(range(len(cache) - 1)):
            for col in reversed(range(len(cache[0]) - 1)):
                if word2[row] == word1[col]:
                    cache[row][col] = cache[row + 1][col + 1]
                else:
                    cache[row][col] = 1 + min(cache[row + 1][col], cache[row + 1][col + 1], cache[row][col + 1])
        
        return cache[0][0]

