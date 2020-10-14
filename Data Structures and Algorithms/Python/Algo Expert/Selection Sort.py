# O(n^2) Time || O(1) Space
from typing import  List
def SelectionSort( array: List[int] ) -> List[int]:
    for i in range(len(array)):
        largest = 0
        for j in range(1, len(array)-i):
            if array[j] > array[largest]:
                largest = j
        array[len(array)-i-1], array[largest] = array[largest], array[len(array)-i-1]
        
    return array

print(SelectionSort([2,1,4,3]))    
        