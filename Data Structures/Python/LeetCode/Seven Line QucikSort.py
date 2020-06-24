import random

# Expected  : O(nlogn) Time || O(n) Space
# Worst     : O(n^2) Time || O(n^2) Space
def QuickSort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)

    lt = [el for el in array if el < pivot]
    eq = [el for el in array if el == pivot]
    gt = [el for el in array if el > pivot]

    return QuickSort(lt) + eq + QuickSort(gt)


print(QuickSort([10, -2, 1, 16, 32, 18, 11, 9]))
