


def squaredArray(array):
    result = [0 for num in array] # [0, 0, 0, 0, 0]

    leftIdx = 0     # 1
    rightIdx = len(array) - 1   # 1

    for idx in reversed(range(0, len(result))): # 0
        leftNum = array[leftIdx]    # -4
        rightNum = array[rightIdx]  # -4
        if abs(leftNum) > abs(rightNum):
            result[idx] = leftNum ** 2
            leftIdx = leftIdx + 1
        else:
            result[idx] = rightNum ** 2
            rightIdx = rightIdx - 1
    return result







sqArray = squaredArray([-10, -4, 1, 2, 5, 8])
print(sqArray)