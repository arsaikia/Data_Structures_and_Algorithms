'''
Algoexpert Easy poblems
'''

from typing import List




#----------------------------------------< TWO SUM >-------------------------------------------------------

# Naive Two sum
# O(n^2) Time | O(1) Space (excluding Results array)
def naiveTwoSum(array: List[int], target: int) -> List[List]:
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                result.append([array[i], array[j]])
    return result

# O(nlogn) Time | O(1) Space
def twoPointerTwoSum(array: List[int], target: int) -> List[List]:
    # To use two pointer method, we need to sort the array
    array.sort()        # O(nlog(n)) Time | O(n log n) Space
    leftPtr, rightPtr = 0, len(array) - 1
    result = []
    while leftPtr < rightPtr:
        if array[leftPtr] + array[rightPtr] == target:
            result.append([array[leftPtr], array[rightPtr]])
            leftPtr += 1
            rightPtr -= 1
        elif array[leftPtr] + array[rightPtr] > target:
            rightPtr -= 1
        else:
            leftPtr += 1
    return result

# O(n) Time | O(n) Space
def twoSum(array: List[int], target: int) -> List[List]:
    complements = {}
    result = []
    for num in array:
        required = target - num
        if required in complements:
            result.append([num, required])
        else:
            complements[num] = True
    return result


#----------------------------------------< Validate Subsequence >------------------------------------------

def validateSubsequence( array, sequence ) -> bool:
    arrIdx, seqIdx = 0, 0
    while seqIdx < len(sequence) and arrIdx < len(array):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)
    





if __name__ == "__main__":
    array = [2, -1, 4, 6, 10, 13]
    target = 12
    # print(naiveTwoSum(array, target))
    # print(twoPointerTwoSum(array, target))
    # print(twoSum(array, target))
    
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    seq = [1, 6, -1, 10]
    print(validateSubsequence(arr, seq))
    
