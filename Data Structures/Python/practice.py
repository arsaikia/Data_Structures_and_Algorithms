# def twoSum(arr, target):
#     i = 0
#     j = len(arr)-1
#     arr.sort()
#     while(i < j):
#         if((arr[i] + arr[j]) == target):
#             return (i, j)
#         if((arr[i] + arr[j]) > target):
#             j -= 1
#         elif((arr[i] + arr[j]) < target):
#             i += 1
#     return "Not Found"


# if __name__ == "__main__":
#     arr = [1, 2, 6, 4, 8, 10]
#     target = [10, 12, 14]
#     for each in target:
#         print(twoSum(arr, each))
    
#     # enumerate
#     for val,index in enumerate(arr):
#         print(val, index)

#       [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

import random
array = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]
sortedArray = sorted(array, key=lambda each : each[0], reverse=True)
for i in range(1, len(sortedArray)):
    if sortedArray[i-1][0] == sortedArray[i][0] and sortedArray[i-1][1] > sortedArray[i][1]:
        sortedArray[i-1][1], sortedArray[i][1] = sortedArray[i][1], sortedArray[i-1][1]
opArr = []
for each in sortedArray:
    opArr.insert(each[1], each)



print(sortedArray)
