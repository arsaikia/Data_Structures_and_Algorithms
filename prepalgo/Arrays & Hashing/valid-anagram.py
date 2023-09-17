class Solution:
    # O(N) Time | O(N) Space
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sCount = [0 for __ in range(26)]
        tCount = [0 for __ in range(26)]

        for idx in range(len(s)):   # O(N) Time
            sCharIdx = ord(s[idx]) - ord("a")
            sCount[sCharIdx] += 1

            tCharIdx = ord(t[idx]) - ord("a")
            tCount[tCharIdx] += 1

        return sCount == tCount  # O(N) Time
