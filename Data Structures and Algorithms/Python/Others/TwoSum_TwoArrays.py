"""
    Given a target value find it from two Input arrays in Linear time
"""
def twoSumAdv( array1, array2, target):
    complementDict = {}
    for each in array1:
        complementDict[target-each] = 1
    for each in array2:
        if each in complementDict:
            return True
    return False

arr1 = [2,4,7,21]
arr2=[-1, 3, 98, 8, 21]
target = 12
print(twoSumAdv(arr1, arr2, target))


