# --------------------------------------<  Two Sum  >---------------------------------

# O(n) Time | O(n) Space
def twoSum(array, target):

    visited = {}

    for idx, num in enumerate(array):
        required = target - num
        if required in visited:
            return True
        else:
            visited[num] = idx
    return False


# O(n) Time | O(1) Space
def validateSubsequence( array, sequence ):
    arrayIdx = sequenceIdx = 0

    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)




if __name__ == "__main__":
    pass
