# O(N) Time | O(N) Space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, size = set(nums), 0

        for num in nums:
            currSize = 0
            if num - 1 not in numsSet:
                while num in numsSet:
                    num += 1
                    currSize += 1
            size = max(size, currSize)

        return size
