# Inefficient
def searchInsertPosition(nums, target):
    idx = 0
    for each in nums:
        if each == target: return nums.index(each)
        elif each > target: return idx
        else: idx += 1
    return idx

# Using Binary Search



nums = [1,3,5,6]
target = 10
print(searchInsertPosition(nums, target))