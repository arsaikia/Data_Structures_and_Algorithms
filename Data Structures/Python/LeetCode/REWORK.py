'''
Contiguous Array : Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
'''
from typing import List

class Solution:
    def findMaxLength(self, nums : List[int]) -> int :
        totalSum = 0
        globalMax = 0
        myDict = {0 : -1}

        for i in range(len(nums)):
            totalSum = (totalSum-1) if nums[i]==0 else (totalSum+1)
            nums[i] = totalSum
            if(totalSum in myDict.keys()): globalMax = max(globalMax, (i-myDict[totalSum]))
            else: myDict[totalSum] = i

        return globalMax





if __name__ == "__main__":
    sol = Solution()
    arr = [0,0,1]
    print(f'Max Length of the binary array {arr} is : {sol.findMaxLength(arr)}')
