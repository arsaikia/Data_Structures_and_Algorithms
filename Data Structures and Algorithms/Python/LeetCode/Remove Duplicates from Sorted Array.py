from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)

    def removeDup(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))


if __name__ == "__main__":
    array = [1, 1, 2, 2, 3, 4, 4]
    array1 = [1, 1, 2, 2, 3, 4, 4]

    sol = Solution()
    sol.removeDuplicates(array)
    print(array)
    sol.removeDup(array1)
    print(array)

    arr = [1,2,3]

    x = set(arr)

    print(set(arr))