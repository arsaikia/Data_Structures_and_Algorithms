# O(N) Time | O(1) Space
class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            left, right = height[l], height[r]
            minCommonHeight = min(leftMax, rightMax)
            waterLeft = minCommonHeight - left
            waterRight = minCommonHeight - right
            res = res + waterLeft if waterLeft > 0 else res
            res = res + waterRight if waterRight > 0 else res

            leftMax = max(leftMax, left)
            rightMax = max(rightMax, right)

            if left < right:
                l += 1
            else:
                r -= 1
        
        return res