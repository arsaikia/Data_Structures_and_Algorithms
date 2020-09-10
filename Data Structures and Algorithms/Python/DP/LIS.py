def longestIncreasingSubsequence(array):
    sequence = [None for i in array]
    maxIdx = 0
    longest = [1 for i in array]

    for i in range(len(array)):
        for j in range(0, i):
            prev = array[j]
            curr = array[i]
            if prev < curr and longest[j] + 1 >= longest[i]:
                longest[i] = 1 + longest[j]
                sequence[i] = j
        if longest[i] >= longest[maxIdx]:
            maxIdx = i

    return buildSequence(array, sequence, maxIdx)


def buildSequence(array, sequence, maxIdx):
    seq = []

    while maxIdx is not None:
        seq.append(array[maxIdx])
        maxIdx = sequence[maxIdx]

    return list(reversed(seq))


if __name__ == "__main__":
    array = [5]
    print(longestIncreasingSubsequence(array))
