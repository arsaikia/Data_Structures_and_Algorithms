from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        frontMult = [1 for i in range(len(nums))]
        backMult = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            if i == 1:
                frontMult[i] = nums[0]
            else:
                
                frontMult[i] = nums[i-1] * frontMult[i-1]
                

        for i in range(len(nums)-2, -1, -1):
            
            if i == len(nums)-2:
                backMult[ len(nums)-2] = nums[len(nums)-1]
            else:
                backMult[i] = nums[i+1] * backMult[i+1]
            

        return [frontMult[i]*backMult[i] for i in range(len(frontMult))]


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
