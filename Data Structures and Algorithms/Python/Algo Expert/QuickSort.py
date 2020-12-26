import random as R

def quickSort( array ):
    quickSortHelper( 0, len(array) - 1, array)
    return array

def quickSortHelper( startIdx, endIdx, arr ):
    if startIdx > endIdx:
        return
    pivot = R.randint(startIdx, endIdx)
    swap(pivot, startIdx, arr)
    pivot = startIdx
    left = startIdx + 1
    right = endIdx

    while left <= right:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            swap(left, right, arr)
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1

    swap(pivot, right, arr)

    isLeftSmaller = (right - 1) - startIdx < endIdx - (right + 1)

    if isLeftSmaller :
        quickSortHelper(startIdx, right - 1, arr)
        quickSortHelper(right + 1, endIdx, arr)
    else:
        quickSortHelper(right + 1, endIdx, arr)
        quickSortHelper(startIdx, right - 1, arr)
    


def swap( i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]




print(quickSort([2, 4, 2, 3, 8, 6, 5, 9, 12, -1]))
