# O(n^2) Time || O(1) Space
def InsertionSort( array ):
    for i in range(1, len(array)):
        for j in range(i, len(array)):
            temp = array[j]
            while j > 0 and array[j-1] > array[j]:
                array[j] = array[j-1]
                j -= 1
            array[j] = temp
    return array

print(InsertionSort([2,1,3]))
            
        