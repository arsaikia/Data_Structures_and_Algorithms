from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costDiff = ([each[0]-each[1] for each in costs])
        arrLen = len(costs)
        indices =  sorted(range(0, arrLen), key=lambda k:costDiff[k])

        minCost = 0

        for i in range(arrLen//2):
            minCost += costs [indices[i]] [0]
            minCost += costs [indices[arrLen-i-1]] [1] 
        return minCost


        

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))