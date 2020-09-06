'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        outputArray = [i+1 for i in range(len(nums))]
        for each in nums:
            if each in outputArray:
                outputArray.pop(outputArray.index(each))

        return outputArray



if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
