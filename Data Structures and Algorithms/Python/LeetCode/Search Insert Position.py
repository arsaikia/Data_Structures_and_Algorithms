# Inefficient
def searchInsertPositionX(nums, target):
    idx = 0
    for each in nums:
        if each == target: return nums.index(each)
        elif each > target: return idx
        else: idx += 1
    return idx

# Using Binary Search
def searchInsertPosition(nums, target):
    start, end = 0, len(nums)
    while start < end:
        
        potentialValue = (start+end)//2
        if target < nums[potentialValue] :
            end = potentialValue
        elif target > nums[potentialValue] :
            start = potentialValue+1
        else:
            return potentialValue
    return start


nums = [1,3,5,6]
target = 9
print(searchInsertPosition(nums, target))