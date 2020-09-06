'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


def subsets(nums):
    powerset = [[]]
    for each in nums:
        for i in range(len(powerset)):
            curr = powerset[i]
            powerset.append(curr + [each])
    return powerset

print(subsets([1,2,3]))
