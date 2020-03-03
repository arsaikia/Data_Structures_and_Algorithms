'''
Modified Bubble Sort:   Worst time      O(N^2)
                        Average time    O(N^2)
                        Best time       O(N)
'''

from typing import List, Dict, Set
import random as R
import time as T


def main():

    array = [R.randint(-1000, 1000) for i in range(R.randint(5000, 10000))]
    startTime = T.time()
    bubbleSort(array)
    endTime = T.time()
    print(f"'Bubble sort' \t\t({len(array)} elements)\t=>  {endTime-startTime}")
    
    startTime = T.time()
    selectionSort(array)
    endTime = T.time()
    print(f"'Selection sort' \t({len(array)} elements) =>  {endTime-startTime}")


def bubbleSort(arr: List[int]) -> None:
    flag = True
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if (arr[j+1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = False

        if flag:
            print("Alreay Sorted!")
            break

def selectionSort(arr: List[int]):

    flag = True

    for i in range(len(arr)-1, -1, -1):
        #print(i)
        largest = arr[0]
        for j in range(0, i):
            if ((arr[j+1] > largest) and (j<len(arr)-1)):
                largest = arr[j+1]
                flag = False
        arr[i], largest = largest, arr[i]
        if(flag): 
            print("Alreay Sorted!")
            break
        
    


if __name__ == "__main__":
    main()
