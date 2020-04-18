'''
🎈🎈
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        zero = 0
        one = 0
        c = 0
        g = 0

        for each in nums:
            if(each == 0):
                zero += 1
            else:
                one += 1

            if(zero == one):
                c += 2
            if(c % 2 == 0):
                g += c
        return g


if __name__ == "__main__":
    sol = Solution()
    Input = [0, 1, 1, 0, 1, 1, 1, 0]
    Input1 = [0, 0, 1, 0, 0, 0, 1, 1]
    for i in range(0, len(Input1)):
        print(sol.findMaxLength(Input1[i:]))
