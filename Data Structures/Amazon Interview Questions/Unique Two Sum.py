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

def uniqueTwoSum( nums, target ):
    found=[]
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
    ans = set()
    comp = set()
    for num in nums:
        c = target - num
        if c in comp:
            res = (num, c) if num > c else (c, num)
            ans.add(res)       
        comp.add(num)
    return len(ans)





if __name__ == "__main__":
    nums = [1, 1, 2, 45, 46, 46]
    target = 47

    nums1 = [1, 5, 1, 5]
    target1 = 6
    print(uniqueTwoSum(nums1, target1))