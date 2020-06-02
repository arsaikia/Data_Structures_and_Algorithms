from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        outputArray = []

        for each in nums:

            if nums[abs(each)-1] > 0:
                nums[abs(each)-1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0: outputArray.append(i+1) 
        return outputArray





if __name__ == "__main__":
    sol= Solution()
    print(sol.findDisappearedNumbers( [1,1,2,2] ))