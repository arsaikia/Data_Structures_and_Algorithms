'''
Find the largest positive intger that does not appear in the input array
e.g:    [-1, -5, 10, 12, 1, 2, 5] => 3
        [-2, -1, 0, 1, 2, 4, 5]  => 3

'''


from typing import List
import random as R


def main():
    array = [R.randint(-10, 10) for i in range(R.randint(5, 10))]

    print(
        f'The largest positive integer from {array} is : {giveLargestInteger(array)}')


def giveLargestInteger(arr: List[int]):

    returnVal: int = 1
    flag = False
    arr.sort()
    print(arr)
    for each in arr:
        if(each < 0):
            continue
        elif (each == 1):
            flag = True
        elif((arr.index(each) < len(arr)-1) and flag):
            if(arr[arr.index(each)+1] != each+1):
                returnVal = (each+1)
                break
    return (returnVal)


if __name__ == "__main__":
    main()
