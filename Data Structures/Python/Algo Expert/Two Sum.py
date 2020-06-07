from typing import List
def NaiveTwoSum( array: List[int] , target) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    Args:
        array (List[int]): Takes an aray of Integers
        target ([type]): Target values to be sum of array elements

    Returns:
        List[int]: Array of indices that give the sum
    
    O(n^2) Time || O(1) Space
    """    
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]
    return -1

def twoPointerTwoSum(array: List[int] , target) -> List[int]:
    array = sorted(array)
    start, end = 0, len(array)-1
    while start < end:
        if array[start]+array[end] > target:
            end -= 1
        elif array[start]+ array[end] < target:
            start += 1
        else:
            return [start, end]
    return -1


print(NaiveTwoSum([1,2,4,6,10,12], 12), twoPointerTwoSum([1,2,4,6,10,12], 12))
            
        
