def findThreeLargestNumbers( array ):
    threeLargest = [ float('-inf') for i in range(3)]
    for each in array:
        getThreeLargest( threeLargest, each)
    return threeLargest

def getThreeLargest( array, num):
    if num > array[2]:
        shiftAndUpdate( array, num, 2)
    elif num > array[1]:
        shiftAndUpdate( array, num, 1)
    elif num > array[0]:
        shiftAndUpdate(array, num, 0)
    return

def shiftAndUpdate( array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[idx] = num
        else:
            array[i] = array[i+1]
    return

print(findThreeLargestNumbers( [12, 22, 1, 99, 126, 4, 187, 9, 321, 320, 325, 90] ))
