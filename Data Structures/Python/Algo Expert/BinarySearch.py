'''
Iterative Approach: 
    Time Complexity : O( log N )
    Space Complexity : O (1)
'''

def binarySearch(array, target):

    start = 0
    end = len(array)-1

    while(start < end):
        potentialValue = start+end // 2
        if array[potentialValue] == target:
            return potentialValue
        elif array[potentialValue] < target:
            start = potentialValue
        else:
            end = potentialValue

    return -1


print(binarySearch([1, 2, 3, 4, 5], 3))
