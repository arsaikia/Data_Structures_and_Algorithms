from typing import List
def sortedSquareArray( array : List[int]) -> List[int] :
    """
    O(n) Time || O(n) Space
    [Takes an sorted integer array and returns sorted array with square of the elements ]

    Args:
        array (List[int]): Sorted integer input array

    Returns:
        List[int]: Sorted Integer output array
        
    [-6, -4, 1, 2, 3, 5]
    """      
    outputArray = []
    start, end = 0, len(array)-1
    while start < end:
        if abs(array[start]) > abs(array[end]):
            outputArray.insert(0, array[start]**2)
            start += 1
        elif abs(array[start]) < abs(array[end]):
            outputArray.insert(0, array[end]**2)
            end -= 1
        else:
            outputArray.insert(0, array[start]**2)
            start += 1
            outputArray.insert(0, array[end]**2)
            end -= 1
    if start == end:
        outputArray.insert(0, array[start])
    return outputArray

myArray = [-6, -4, 1, 2, 3, 5]
print(sortedSquareArray(myArray))