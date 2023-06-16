
# O(N) Time | O(N) Space
class Solution:
    def containsDuplicate(self, nums) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)


allNums = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
]
nums = [1, 2, 3, 1]
solution = Solution()

for nums in allNums:
    hasDuplicate = solution.containsDuplicate(nums)
    print('List -> ${[1, 2, 3, 1]}',
          'has duplicate \n' if hasDuplicate else 'doesn\'t have duplicates \n')
