def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    maxArray = nums[:]
    maxArray[1] = max(maxArray[0], maxArray[1])
    for i in range(2, len(nums)):
        maxArray[i] = max(maxArray[i] + maxArray[i-2], maxArray[i-1])
    return maxArray[-1]
