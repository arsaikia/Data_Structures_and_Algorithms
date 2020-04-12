'''
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    ```
    Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                Not 7-1 = 6, as selling price needs to be larger than buying price.
    ```
    ```
    Example 2:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
    ```
    
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
