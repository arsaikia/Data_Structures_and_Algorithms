'''
    🐲🐲 🐲🐲
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Example:

        ```
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        ```
    
    __Note:__
        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.

    🐲🐲🐲🐲
'''


def moveZeroes(nums):

    indxArr = []
    zeroCounter = 0

    for i in range(0, len(nums)):
        if(nums[i] == 0):
            zeroCounter += 1
        else:
            indxArr.append(i)

    for i in range(0, len(indxArr)):
        nums[i] = nums[indxArr[i]]

    for i in range(len(nums)-1, len(indxArr)-1, -1):

        nums[i] = 0


if __name__ == "__main__":
    nums = [0, 1, '🤪', 0]
    moveZeroes(nums)
    print(nums)
