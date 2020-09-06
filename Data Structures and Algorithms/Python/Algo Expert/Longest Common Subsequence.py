

import numpy as np


'''
Top Down : O( mn ) Time | O(mn)  Space

Approach:   Check if the last elements are same, if yes count = 1 and recursively check for other elements
            else, result will be max of the twos string with a character removed from either of them
            At any point, if we when we are done with a check, we update the cache to store max value at that index

'''


def LCS(string1, string2, m, n, cache):
    if m <= 0 or n <= 0:
        return 0
    if cache[m][n]:
        return cache[m][n]

    if string1[n - 1] == string2[m - 1]:
        count = 1 + LCS(string1, string2, m - 1, n - 1, cache)
    else:
        count = max(LCS(string1, string2, m - 1, n, cache),
                    LCS(string1, string2, m, n - 1, cache))
    cache[m][n] = count

    return count


def findSequence(string, cache):
    row = len(cache) - 1
    col = len(cache[0]) - 1
    sequence = []

    while row != 0 or col != 0:
        curr = cache[row][col]
        if curr == cache[row - 1][col]:
            row -= 1
        elif curr == cache[row][col - 1]:
            col -= 1
        else:
            sequence.append(string[col - 1])
            row -= 1
            col -= 1
    return "".join(list(reversed(sequence)))


'''
Bottom Up : O( mn ) Time | O(mn)  Space

Approach:   We traverse from index 0, 0 to end and at each index we check the following:
            1. If the characters at the current index are same, value at the cachec location is:
                1 + cache[i - 1][j - 1]
            2. Else, we need to see max value with two cases:
                a. String1 to the previous index with string2
                b. String2 to the previous index with string1

'''


def longestCommonSubsequence(s1, s2):
    cache = [[0 for col in range(len(s1) + 1)] for row in range(len(s2) + 1)]
    for row in range(1, len(cache)):
        for col in range(1, len(cache[0])):
            if s1[col - 1] == s2[row - 1]:
                cache[row][col] = 1 + cache[row - 1][col - 1]
            else:
                cache[row][col] = max(cache[row - 1][col], cache[row][col - 1])
    return buildSequence(s1, cache)


def buildSequence(string, cache):
    row = len(cache) - 1
    col = len(cache[0]) - 1
    sequence = []
    while row > 0 and col > 0:
        if cache[row][col] == cache[row - 1][col]:
            row -= 1
        elif cache[row][col] == cache[row][col - 1]:
            col -= 1
        else:
            sequence.append(string[col - 1])
            row -= 1
            col -= 1

    return "".join(list(reversed(sequence)))


if __name__ == "__main__":
    string1 = "BATD"
    string2 = "ABACD"
    cache = [[0 for col in range(len(string1) + 1)]
             for row in range(len(string2) + 1)]
    LCS(string1, string2, len(string2), len(string1), cache)
    print(np.array(cache))
    print(findSequence(string1, cache))

    # Bottom Up
    print(longestCommonSubsequence(string1, string2))
