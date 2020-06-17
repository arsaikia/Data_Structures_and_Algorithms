def smallestDifference( array1, array2 ):
    array1.sort() 
    array2.sort() 
    idxOne, idxTwo = 0, 0
    smallestCurrent = float('inf')
    smallestGlobal = float('inf')
    
    while idxOne < len(array1) and idxTwo < len(array2):
        firstElement = array1[idxOne]
        secondElement = array2[idxTwo]
        if firstElement > secondElement:
            smallestCurrent = min(smallestCurrent, firstElement-secondElement)
            idxTwo += 1
        elif secondElement > firstElement:
            smallestCurrent = min(smallestCurrent, secondElement-firstElement)
            idxOne += 1
        else:
            return [firstElement, secondElement]
        
        if smallestCurrent < smallestGlobal:
            smallestGlobal = smallestCurrent
            smallestPair = [firstElement, secondElement]
    return smallestPair


print(smallestDifference([1, 3, 15, 11, 2],[23, 127, 235, 19, 8, 11]))
        