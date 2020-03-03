'''
Modified Bubble Sort:   Worst time      O(N^2)
                        Average time    O(N^2)
                        Best time       O(N)
'''

from typing import List, Dict, Set
import random as R
import time as T


def main():

    startTime = T.time()
    array = [R.randint(-1000, 1000) for i in range(R.randint(5000, 10000))]
    bubbleSort(array)
    endTime = T.time()
    print(
        f'Time taken for Bubble sort to sort {len(array)} elements: {endTime-startTime}')


def bubbleSort(arr: List[int]) -> None:
    flag = True
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if (arr[j+1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = False

        if flag == True:
            print("Alreay Sorted!")
            break


if __name__ == "__main__":
    main()
