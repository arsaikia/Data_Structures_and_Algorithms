# O(logn) Time | O(1) Space
def searchRange(nums, target):
        finalRange = [-1, -1]
        modifiedBinarySearch(nums, 0, len(nums) - 1, target, finalRange, True)
        modifiedBinarySearch(nums, 0, len(nums) - 1, target, finalRange, False)
        return finalRange
    
def modifiedBinarySearch(array, left, right, target, finalRange, goLeft):
    
    while left <= right:
        mid = (left + right) // 2
        potential = array[mid]
        if target < potential:
            right = mid - 1
        elif target > potential:
            left = mid + 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                
                else:
                    left = mid + 1
arr = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45       
print(searchRange(arr, target))
