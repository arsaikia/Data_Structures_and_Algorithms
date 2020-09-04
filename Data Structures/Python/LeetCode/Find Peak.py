from typing import List

class Solution:
    # O(log(n)) Time | O(1) Space
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid + 1] > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1, 2, 4, -1, 21]))
