

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
🎉
'''

from typing import List
import unittest


class Solution:

    # (nlogn) solution usin sort:
    def countElements_NlogN(self, arr: List[int]) -> int:
        arr = sorted(arr)
        count = 0
        globalCount = 0

        for i in range(1, len(arr)):
            if(arr[i] == arr[i-1]):
                count += 1
            elif(arr[i]-1 == arr[i-1]):
                globalCount += max(count+1, 1)
                count = 0
            else:
                count = 0
            if(i == len(arr)-2 and arr[i]-1 == arr[i-1]):
                globalCount += count
        return globalCount

    # (N) solution using hashSet:
    def countElements_N(self, arr: List[int]) -> int:

        my_hashSet = set(arr)
        count = 0

        for each in arr:
            if(each+1 in my_hashSet):
                count += 1

        return count


if __name__ == "__main__":

    sol = Solution()
    arr = [4, 10, 11, 11, 1, 9, 6, 2, 4, 5, 8]
    print(sol.countElements_NlogN(arr) == sol.countElements_N(arr))
