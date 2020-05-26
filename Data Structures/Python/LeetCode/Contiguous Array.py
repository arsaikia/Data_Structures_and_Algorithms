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

        if(len(nums) <= 1):
            return 0

        globalMax = 0
        myDict = {0: -1}
        sums = 0

        for i in range(len(nums)):
            if(nums[i] == 0):
                nums[i] = -1
            sums = sums + nums[i]
            if(sums in myDict.keys()):
                globalMax = max(globalMax, i-myDict.get(sums))
            else:
                myDict[sums] = i
        return globalMax


if __name__ == "__main__":
    # myFile = pd.read_csv("../Test Data/ContiguousArray.csv", sep=',')
    # print(myFile)
    sol = Solution()
    Input = [0, 1, 1, 0, 1, 1, 1, 0]
    Input1 = [0, 0, 1, 0, 0, 0, 1, 1]
    print(f'Max Length is: {sol.findMaxLength([0,0,1])}')
