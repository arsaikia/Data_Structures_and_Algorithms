from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = -1
        isGreatest = []

        for each in candies:
            if each > max:
                max = each

        for each in candies:
            isGreater = False
            if (extraCandies + each >= max):
                isGreater = True
            isGreatest.append(isGreater)
        return isGreatest


if __name__ == "__main__":
    sol = Solution()
    print(f'The output is : {sol.kidsWithCandies([2,3,5,1,3], 3)}')
