# BRUTE FORCE | TLE
# O(2^max(m, n)) Time - m, n : size of s1, s2
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def recursiveBruteForce(i, j):
            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True

            if i < len(s1) and i + j < len(s3) and s1[i] == s3[i + j] and recursiveBruteForce(i + 1, j):
                return True

            if j < len(s2) and i + j < len(s3) and s2[j] == s3[i + j] and recursiveBruteForce(i, j + 1):
                return True
            
            return False
            
        return recursiveBruteForce(0, 0)


################################################################################
# Top Down recursive DP | Accepted
# O(m + n) Time
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        
        def topDownDP(i, j):

            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            if i < len(s1) and i + j < len(s3) and s1[i] == s3[i + j] and topDownDP(i + 1, j):
                return True

            if j < len(s2) and i + j < len(s3) and s2[j] == s3[i + j] and topDownDP(i, j + 1):
                return True
            
            cache[(i, j)] = False
            
            return False
            
        return topDownDP(0, 0)
    

################################################################################
# Bottom Up
# O(M x N) Time | O(M x N) Space
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False for __ in range(len(s2) + 1)] for __ in range(len(s1) + 1) ]
        dp[-1][-1] = True

        for i in reversed(range(len(s1) + 1)):
            for j in reversed(range(len(s2) + 1)):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        
        return dp[0][0]

################################################################################