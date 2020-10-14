'''
Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0


'''


def getMinInRotatedSortedArray(array):
    if len(array) == 1 or array[0] < array[-1]:
        return array[0]

    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        potential = array[mid]

        if potential > array[mid + 1]:
            return array[mid + 1]

        if array[mid - 1] > potential:
            return potential

        if array[start] < potential:
            start = mid + 1
        else:
            end = mid - 1


if __name__ == "__main__":
    array = [4, 5, -2, -1, 0, 1, 2]
    print(getMinInRotatedSortedArray(array))
