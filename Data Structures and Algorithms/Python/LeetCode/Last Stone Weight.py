

'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

'''
from typing import List


class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return stones[0]
        self.h = []
        for each in stones:
            self.heapq.heappush(self.h, -1 * each)

        while(len(self.h) != 1):
            print(self.h)
            maxVal, minVal = -1 * \
                self.heapq.heappop(self.h), -1 * self.heapq.heappop(self.h)
            self.heapq.heappush(
                self.h, (minVal-maxVal))
        return -self.h[0]


if __name__ == "__main__":

    Input = [2, 7, 4, 1, 8, 1]
    sol = Solution()
    print(sol.lastStoneWeight(Input))



