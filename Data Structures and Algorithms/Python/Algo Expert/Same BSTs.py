def sameBsts(arrayOne, arrayTwo):

    if len(arrayOne) == 0:
        return True

    if arrayOne[0] != arrayTwo[0] or len(arrayOne) != len(arrayTwo):
        return False

    leftOne = getSmallerThan(arrayOne)
    rightOne = getGreaterThan(arrayOne)
    leftTwo = getSmallerThan(arrayTwo)
    rightTwo = getGreaterThan(arrayTwo)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def getSmallerThan(array):
    return [array[i] for i in range(1, len(array)) if array[i] < array[0]]

def getGreaterThan(array):
    return [array[i] for i in range(1, len(array)) if array[i] >= array[0]]


print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11],
               [10, 8, 5, 15, 2, 12, 11, 94, 81]))
