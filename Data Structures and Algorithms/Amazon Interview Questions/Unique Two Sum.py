'''
Given an int array nums and an int target, 
find how many unique pairs in the array such that their sum is equal to target. 
Return the number of pairs.

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
'''


def uniqueTwoSum(nums, target):
    found = []
    complementDict = {}
    for num in nums:
        required = target - num
        if required in complementDict and [required, num] not in found:
            found.append(sorted([required, num]))
        else:
            complementDict[num] = True
    return len(found)


# More Efficient Solution
def uniquePairs(nums, target):
    found = set()
    complementSet = set()
    for num in nums:
        complement = target - num
        if complement in complementSet:
            result = (num, complement) if num > complement else (
                complement, num)
            found.add(result)
        complementSet.add(num)
    return len(found)


if __name__ == "__main__":
    nums = [1, 1, 2, 45, 46, 46]
    target = 47

    nums1 = [1, 5, 1, 5]
    target1 = 6
    print(uniqueTwoSum(nums1, target1) == uniquePairs(nums1, target1))
