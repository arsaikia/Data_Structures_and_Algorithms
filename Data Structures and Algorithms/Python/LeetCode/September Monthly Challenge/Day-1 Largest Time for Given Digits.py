'''
https://leetcode.com/problems/largest-time-for-given-digits/
'''

from itertools import permutations
from typing import List

# O(1) Time | O(1) Space


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1

        for h, i, j, k in permutations(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    Sol = Solution()
    print(Sol.largestTimeFromDigits(array))
