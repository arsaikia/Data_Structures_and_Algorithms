# O(n^2) Worst Time Complexity || O(1) Space Complexity
# O(n) Average time complexity
def BubbleSort( array ):
    isSwapped = False
    for i in range(len(array)):
        for j in range(1, len(array)-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] =  array[j], array[j-1]
                isSwapped = True
        if isSwapped == False:
            break
    return array
        
print(BubbleSort([1,2,3]))
