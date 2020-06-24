# O(n) Time || O(n) Space
def maxSubsetNoAdjacent(array):
    if not len(array):
        return
    
    maxSums = array[:]
    for i in range(2, len(array)):
        array[i] = max(array[i-1], array[i] + array[i-2])
    return array[-1]
        

# O(n) time || O(1) Space
def maxSubsetNoAdjacent(array):
    if len(array) <= 1:
        return array
    
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        curr = max(first, second+array[i])
        second = first
        first = curr
    return first




print(maxSubsetNoAdjacent([7, 10, 12, 7, 9, 14]))
