
'''
🙈 
Selection Sort:   Worst time      O(N^2)
                        Average time    O(N^2)
                        Best time       O(N)
'''

from typing import List, Dict, Set
import random as R
import time as T


def main():

    startTime = T.time()
    #array = [R.randint(-1000, 1000) for i in range(R.randint(5000, 10000))]
    array = [1, 9, -1, 2]
    selectionSort(array)
    endTime = T.time()
    print(
        f'Time taken for Selection sort to sort {len(array)} elements: {endTime-startTime}')


def selectionSort(arr: List[int]) -> None:
    print("🙋  ❗")
    
    


if __name__ == "__main__":
    main()
