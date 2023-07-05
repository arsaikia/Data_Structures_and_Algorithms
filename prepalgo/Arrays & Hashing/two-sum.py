class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for idx, num in enumerate(nums):
            required = target - num
            if required in visited:
                return [visited[required], idx]
            visited[num] = idx

        return [-1, -1]
