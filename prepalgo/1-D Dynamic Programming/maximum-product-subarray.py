# O(N) Time | O(1) Space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxSubarrayProduct, minSubarrayProduct = 1, 1

        for num in nums:
            currMax = maxSubarrayProduct
            maxSubarrayProduct = max( (maxSubarrayProduct * num), (minSubarrayProduct * num), num )
            minSubarrayProduct = min( (currMax * num), (minSubarrayProduct * num), num)
            res = max(maxSubarrayProduct, res)
        
        return res