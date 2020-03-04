'''
'Bubble sort' 		(8354 elements)	=>  3.779292345046997
'Selection sort' 	(8354 elements) =>  1.905583143234253
'Insertion sort' 	(8354 elements)	=>  1.8939638137817383 
'Merge sort' 		(8354 elements)	=>  0.022716045379638672
'''

from typing import List, Dict, Set
import random as R
import time as T
import matplotlib.pyplot as plt
import copy as cp


def main():

    # The array to be sorted
    array = [R.randint(-1000, 1000) for i in range(R.randint(8000, 10000))]
    arr1 = cp.deepcopy(array)
    arr2 = cp.deepcopy(array)
    arr3 = cp.deepcopy(array)
    arr4 = cp.deepcopy(array)

    # Bubble Sort
    startTime = T.time()
    bubbleSort(arr1)
    endTime = T.time()
    bTime = endTime-startTime
    print(
        f"'Bubble sort' \t\t({len(arr1)} elements)\t=>  {bTime}")

    # Selection Sort
    startTime = T.time()
    selectionSort(arr2)
    endTime = T.time()
    sTime = endTime-startTime
    print(
        f"'Selection sort' \t({len(arr2)} elements) =>  {sTime}")

    # Insertion Sort
    startTime = T.time()
    insertionSort(arr3)
    endTime = T.time()
    iTime = endTime-startTime
    print(
        f"'Insertion sort' \t({len(arr3)} elements)\t=>  {iTime} ")

    # Merge Sort
    startTime = T.time()
    mergeSort(arr4)
    endTime = T.time()
    mTime = endTime-startTime

    print(
        f"'Merge sort' \t\t({len(arr4)} elements)\t=>  {mTime} ")

    # Comparision Plot
    plt.plot([bTime, sTime, iTime, mTime])
    plt.show()


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
        # print(i)
        largest = arr[0]
        for j in range(0, i):
            if ((arr[j+1] > largest) and (j < len(arr)-1)):
                largest = arr[j+1]
                flag = False
        arr[i], largest = largest, arr[i]
        if(flag):
            print("Alreay Sorted!")
            break


def insertionSort(arr: List[int]):

    for i in range(1, len(arr)):
        swapped = False
        newElement = arr[i]
        while((newElement < arr[i-1]) and (i > 0)):
            arr[i] = arr[i-1]
            i -= 1
            swapped = True
        if(swapped):
            arr[i] = newElement
    # print(arr)


def mergeSort(arr):                 # [1, 2, 3, 4, 5]

    mid = len(arr)//2               # 2
    if(mid > 0):
        L = arr[:mid]               # [1, 2]
        R = arr[mid:]      # [3, 4, 5]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while((i < len(L)) and (j < len(R))):
            if(L[i] < R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while((i < len(L))):
            arr[k] = L[i]
            i += 1
            k += 1

        while((j < len(R))):
            arr[k] = R[j]
            k += 1
            j += 1

    # print(arr)


if __name__ == "__main__":
    main()
