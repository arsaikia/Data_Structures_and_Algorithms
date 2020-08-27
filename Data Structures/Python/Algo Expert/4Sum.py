
class Solution:
    def fourSum(self, nums, target):
        allSums = {}
        quadruplets = []
        for i in range(1, len(nums)-1):
            currNum = nums[i]
            for j in range(i+1, len(nums)):
                runningNum = currNum + nums[j]
                required = target - runningNum
                if required in allSums:
                    for child in allSums[required]:
                        quad = [currNum, nums[j]] + child
                        quad.sort()
                        if quad not in quadruplets:
                            quadruplets.append(quad)

            for k in range(0, i):
                toAdd = nums[k] + currNum
                if toAdd not in allSums:
                    allSums[toAdd] = [[nums[k], currNum]]
                else:
                    allSums[toAdd].append([nums[k], currNum])

        return quadruplets


fourSum = Solution()
nums = [-5, 5, 4, -3, 0, 0, 4, -2]
target = 4
print(fourSum.fourSum(nums, target))
