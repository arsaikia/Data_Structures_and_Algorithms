

'''
🎉
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
'''

from typing import List

# nlogn solution usin sort:


class Solution:
    def countElements(self, arr: List[int]) -> int:

        arr.sort()
        #arr = list(set(arr))
        print(arr)
        currCount = 0
        globalCount = 0

        for i in range(1, len(arr)):
            if(arr[i] == arr[i-1]):
                currCount += 1
            elif(arr[i]-1 == arr[i-1]):
                currCount += 1
                globalCount += 1
            else:
                currCount = 0

        return globalCount



if __name__ == "__main__":

    sol = Solution()
    print(sol.countElements([1, 1, 2, 2]))
