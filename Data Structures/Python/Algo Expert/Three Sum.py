def threeSum(array, target):
    array.sort()
    for idx in range(len(array)):
        start = idx+1
        end = len(array)-1
        required = target - array[idx]
        while start < end:
            if array[start] + array[end] < required:
                start += 1
            elif array[start] + array[end] > required:
                end -= 1
            else:
                return {array[idx]: idx, array[start]: start, array[end]: end}
    return -1


print(threeSum([1, 2, 4, 5, 6, 10, 8, 12], 18))
