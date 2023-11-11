
def N_sum(nums, target, n):
    if n == 2:
        return TwoSum(nums, target)
    else:
        res = []
        prev = None
        for i in range(len(nums) - n + 1):
            if nums[i] != prev:
                cur_sum = N_sum(nums[i+1:], target-nums[i], n-1)
                for j in cur_sum:
                    j.append(nums[i])
                res.extend(cur_sum)
                prev = nums[i]

        return res


def TwoSum(nums, target):
    L = 0
    R = len(nums)-1
    res = []
    while L < R:
        temp = nums[L] + nums[R]
        if temp == target:
            res.append([nums[L], nums[R]])
            L += 1
            R -= 1
            while L < R and nums[L] == nums[L-1]:
                L += 1
            while L < R and nums[R] == nums[R+1]:
                R -= 1
        elif temp < target:
            L += 1
        elif temp > target:
            R -= 1
    return res


nums = [1, 2, 4, 10, 12, 22, -100, -21, 21, 2, 2, 3, 1]
res = N_sum(nums, 10, 7)
print(res)
