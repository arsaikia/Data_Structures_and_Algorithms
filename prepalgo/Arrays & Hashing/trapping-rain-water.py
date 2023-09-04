# O(N) Time | O(N) Space
class Solution:
    def trap(self, height: List[int]) -> int:
        maxheightToLeft = [0 for __ in height]
        maxheightToRight = [0 for __ in height]

        for i in range(1, len(height)):
            maxheightToLeft[i] = max(maxheightToLeft[i-1], height[i-1])

        for i in reversed(range(len(height) - 1)):
            maxheightToRight[i] = max(maxheightToRight[i+1], height[i+1])

        waterArea = 0

        for idx in range(len(height)):
            maxToLeft = maxheightToLeft[idx]
            maxToRight = maxheightToRight[idx]
            waterCapacityAtIdx = min(maxToLeft, maxToRight) - height[idx]
            waterArea = (
                waterArea + waterCapacityAtIdx) if waterCapacityAtIdx > 0 else waterArea

        return waterArea


##########################################################
# O(N) Time | O(1) Space
class Solution:
    def trap(self, height: List[int]) -> int:
        waterArea = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0

        while left < right:
            leftElevation, rightElevation = height[left], height[right]

            if leftElevation < rightElevation:
                if leftElevation > leftMax:
                    leftMax = leftElevation
                else:
                    waterArea += leftMax - leftElevation
                left += 1
            else:
                if rightElevation > rightMax:
                    rightMax = rightElevation
                else:
                    waterArea += rightMax - rightElevation
                right -= 1
        return waterArea
