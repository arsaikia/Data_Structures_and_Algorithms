# O(nlogn) TIme | O(nlogn) Space
def mergesort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid + 1:]
    return mergeSortedArrays(mergesort(left), mergesort(right))


def mergeSortedArrays(left, right):
    sortedArray = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArray[k] = left[i]
            i += 1
        else:
            sortedArray[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        sortedArray[k] = left[i]
        i += 1
        k += 1

    while i < len(right):
        sortedArray[k] = right[i]
        j += 1
        k += 1
    return sortedArray


# O(nlog(n)) Time | O(n) Space
def mergeSortInPlace(array):
    if len(array) <= 1:
        return array

    auxArray = array[:]
    mergeSortHelper(array, 0, len(array) - 1, auxArray)
    return array


def mergeSortHelper(mainArray, startIdx, endIdx, auxArray):
    if startIdx == endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxArray, startIdx, midIdx, mainArray)
    mergeSortHelper(auxArray, midIdx + 1, endIdx, mainArray)
    doMerge(mainArray, startIdx, midIdx, endIdx, auxArray)


def doMerge(mainArray, startIdx, midIdx, endIdx, auxArray):
    k = startIdx
    i = startIdx
    j = midIdx + 1

    while i <= midIdx and j <= endIdx:
        if auxArray[i] <= auxArray[j]:
            mainArray[k] = auxArray[i]
            i += 1
        else:
            mainArray[k] = auxArray[j]
            j += 1
        k += 1
    while i <= midIdx:
        mainArray[k] = auxArray[i]
        i += 1
        k += 1

    while j <= endIdx:
        mainArray[k] = auxArray[j]
        j += 1
        k += 1
