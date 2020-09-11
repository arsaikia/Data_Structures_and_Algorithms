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


if __name__ == "__main__":
    
    '''Four Number Sum'''
    array = [7, 6, 4, -1, 1, 2]
    target = 16
    print(fourSum(array, target))
