array = [5, 1, 2, 4, 3]

# O(n) time || O(1) Space
def moveElementsToEnd(array, toMove):
    startIdx = 0
    endIdx = len(array)-1

    while startIdx < endIdx:
        if array[endIdx] == toMove:
            endIdx -= 1
        if array[startIdx] != toMove:
            startIdx += 1
        else:
            swap(array, startIdx, endIdx)
            startIdx += 1
            endIdx -= 1

    return array


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


print(moveElementsToEnd(array, 3))
