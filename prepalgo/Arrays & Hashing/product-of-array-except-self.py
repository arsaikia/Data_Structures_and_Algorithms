# O(N) Time | O(N) Space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftMult = [1 for __ in nums] # O(N)
        rightMult = [1 for __ in nums] # O(N)

        runningMult = 1
        
        # O(N)
        for idx in range(1, len(leftMult)):
            runningMult = nums[idx - 1] * runningMult
            leftMult[idx] = runningMult
        
        runningMult = 1
        # O(N)
        for idx in reversed(range(len(rightMult) - 1)):
            runningMult = nums[idx + 1] * runningMult
            rightMult[idx] = runningMult
        
        res = [1 for __ in nums]

        # O(N)
        for idx in range(len(nums)):
            res[idx] = leftMult[idx] * rightMult[idx]
        
        return res

##################################################################
# O(N) Time | O(N) Space - Optimized
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # For each element get the mult of elements to left
        multLeft = [1 for __ in nums]
        for i in range(1, len(nums)):
            multLeft[i] = multLeft[i - 1] * nums[i - 1]

        # For each element get the mult of elements to right
        runningMult = 1
        for i in reversed(range(len(nums) - 1)):
            runningMult = runningMult * nums[i + 1]
            multLeft[i] *= runningMult
        
        return multLeft