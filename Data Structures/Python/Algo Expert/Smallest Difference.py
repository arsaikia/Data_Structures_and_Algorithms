def smallestDifference( array1, array2 ):
    array1.sort()
    array2.sort()
    idxOne, idxTwo = 0, 0
    smallestCurrent = float('inf')
    smallestGlobal = float('inf')
    
    while idxOne < len(array1) and idxTwo < len(array2):
        smallestCurrent = min(smallestCurrent, abs(array1[idxOne] - array2[idxTwo]))
        if array1[idxOne] < array2[idxTwo]:
            idxOne += 1
        elif array1[idxOne] > array2[idxTwo]:
            idxTwo += 1
        else:
            return array1[idxOne],  array2[idxTwo]
        smallestGlobal = min(smallestCurrent, smallestGlobal)
    return smallestGlobal


print(smallestDifference([1, 3, 15, 11, 2],[23, 127, 235, 19, 8]))
        