class Solution:
    # BRUTE FORCE - TLE
    # O(N^3) Time | O(1) Space
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(str, i, j):
            while i <= j:
                if str[i] != str[j]:
                    return False
                i += 1
                j -= 1
            return True

        longest = float("-inf")
        idx = [-1, -1]

        for l in range(len(s)):
            r = l
            while r < len(s):
                if isPalindrome(s, l, r) and r - l > longest:
                    longest = r - l
                    idx= [l, r + 1]
                r += 1
        return s[idx[0] : idx[1]]

###################################################################

# O(N^2) Time | O(1) Space
class Solution:
    def checkPalindrome(self, st, left, right):
        while left > -1 and right < len(st) and st[left] == st[right]:
            left -= 1
            right += 1
        return [left + 1, right]

    def longestPalindrome(self, s: str) -> str:
        longest = float("-inf")
        idx = [-1, -1]
        
        for i in range(len(s)):
            l, r = self.checkPalindrome(s, i, i)
            if r - l > longest:
                longest = r - l
                idx = [l, r]
            
            l, r = self.checkPalindrome(s, i, i + 1)
            if r - l > longest:
                longest = r - l
                idx = [l, r]
        
        return s[idx[0] : idx[1]]    


