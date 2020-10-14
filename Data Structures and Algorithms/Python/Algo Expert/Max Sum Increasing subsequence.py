# O(n^2) Time | O(n) Space
def maxSumIncreasingSubsequence(array):
    sums = array[:]
    sequence = [None for each in array]
    maxSumIdx = 0

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] > array[i]:
                continue
            if array[i] + sums[j] >= sums[i]:
                sums[i] = array[i] + sums[j]
                sequence[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    return buildSequence(array, sequence, maxSumIdx)


def buildSequence(array, seq, maxIdx):
    sequence = []
    while maxIdx is not None:
        sequence.append(array[maxIdx])
        maxIdx = seq[maxIdx]
    return list(reversed(sequence))


if __name__ == "__main__":
    array = [10, 70, 20, 30, 50, 11, 30]
    print(maxSumIncreasingSubsequence(array))
