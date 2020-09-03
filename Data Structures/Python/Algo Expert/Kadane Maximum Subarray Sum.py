'''
Maximum Subarray        https://leetcode.com/problems/maximum-subarray/

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# O(n) Time | O(n) Space 
def maxSubarraySum( array ):
    maxSum = array[:]
    for i in range(1, len(array)):
        maxSum[i] = max(maxSum[i], maxSum[i] + maxSum[i - 1])
    return max(maxSum)




if __name__ == "__main__":
    print(maxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))