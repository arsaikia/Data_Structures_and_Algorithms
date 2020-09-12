# ----------------------------------------< Four Number Sum >-----------------------------------------------
'''
Time Complexity Analysis:
Average: O(n^2) Time    |   O(n^2) Space
        For each value in outer for loop we have two inner forloops which 
        takes n^2 Time each => O(2 n^2) => O(n^2)

Worst:  O(n^3)  |   O(N^2) Space
        In a really worse case where we have values like [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        and target 0, we will have a lot of children in complement hashtable for sum 0 : 
        [ [-1, 1], [-2, 2], [-3, 3], [-4, 4]]
        In such scenarios, the time to traverse through the children will also come into 
        picture making the time complexity more in O(n^3) than O(n^2)
        IN MOST CASES IT WILL BE O(n^2)
  
In both cases we are storing n^2 values in the hashtable, which causes this space complexity.      
'''


def fourSum(array, target):
    complements = {}
    allSums = []
    for i in range(1, len(array) - 1):
        for j in range(i, len(array)):
            required = target - (array[i] + array[j])
            if required in complements:
                for sums in complements[required]:
                    allSums.append([sums + [array[i], array[j]]])
        for k in range(0, i + 1):
            if array[i] + array[k] not in complements:
                complements[array[i] + array[k]
                            ] = [sorted([array[i], array[k]])]
            else:
                complements[array[i] + array[k]
                            ].append(sorted([array[i], array[k]]))

    return allSums


# ----------------------------------------< Subarray Sort >-----------------------------------------------
# O(n) Time | O(1) Space
def subarraysort(array):
    minOutOfPlace = float("inf")
    maxOutOfPlace = float("-inf")

    for idx, num in enumerate(array):
        if isOutOfPlace(array, num, idx):
            minOutOfPlace = min(minOutOfPlace, num)
            maxOutOfPlace = max(maxOutOfPlace, num)

    start, end = 0, len(array) - 1
    while start < len(array):
        if minOutOfPlace > array[start]:
            start += 1
        else:
            break
    while end > -1:
        if maxOutOfPlace < array[end]:
            end -= 1
        else:
            break

    print(start, end)


def isOutOfPlace(array, num, idx):
    if idx == 0:
        return num > array[idx + 1]
    if idx == len(array) - 1:
        return array[idx] < array[len(array) - 2]

    return array[idx - 1] > array[idx] or array[idx + 1] < array[idx]



# ----------------------------------------< Largest Range >-----------------------------------------------
def largestRange(array):
    nums = { num : True for num in array}
    longest = []
    globalMax = float("-inf")
    
    for each in array:
        if each in nums:
            currMax = 1
            left = each - 1
            while left in nums:
                left -= 1
                currMax += 1
            right = each + 1
            while right in nums:
                right += 1
                currMax += 1
            if currMax > globalMax:
                globalMax = currMax
                longest = [left + 1, right - 1]
    return longest







if __name__ == "__main__":

    '''Four Number Sum'''
    # array = [7, 6, 4, -1, 1, 2]
    # target = 16
    # print(fourSum(array, target))

    '''Subarray Sort'''
    # array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    # print(subarraysort(array))
    
    
    '''Largest Range'''
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print(largestRange(array))