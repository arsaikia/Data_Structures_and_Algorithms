import numpy as np
s1 = "BATD"
s2 = "ABACD"
m = len(s1) - 1
n = len(s2) - 1

# O(2^(m+n)) Time || O(2^n) Space


def lcsRecursive(s1, s2, m, n):
    if m < 0 or n < 0:
        return 0

    if s1[m] == s2[n]:
        count = 1 + lcsRecursive(s1, s2, m - 1, n - 1)
    else:
                    lcsRecursive(s1, s2, m, n - 1))
    return count



memo=[[0 for col in range(len(s1) + 1)] for row in range(len(s2) + 1)]

# O(mn) Time | O(mn) Space
def lcsMemoizedRecursive(s1, s2, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if memo[m][n] != 0:
        return memo[m][n]

    if s1[n - 1] == s2[m - 1]:
        count=1 + lcsMemoizedRecursive(s1, s2, m - 1, n - 1, memo)
    else:
        count=max(lcsMemoizedRecursive(s1, s2, m - 1, n, memo),
                    lcsMemoizedRecursive(s1, s2, m, n - 1, memo))
    memo[m][n]=count
    return count


def trverseSubstring(string, memo):
    sequence=[]
    row=len(memo) - 1
    col=len(memo[0]) - 1
    while row > 0 and col > 0:
        if memo[row][col] == memo[row - 1][col]:
            row -= 1
        elif memo[row][col] == memo[row][col - 1]:
            col -= 1
        else:
            sequence.append(string[row - 1])
            row -= 1
            col -= 1
    return "".join(list(reversed(sequence)))

# O(mn) Time | O(mn) Space
def lcsBottomsUp(s1, s2):
    cache=[[0 for col in range(len(s1) + 1)] for row in range(len(s2) + 1)]
    for row in range(1, len(cache)):
        for col in range(1, len(cache[0])):
            if s2[row - 1] == s1[col - 1]:
                cache[row][col]=cache[row - 1][col - 1] + 1
            else:
                cache[row][col]=max(cache[row][col - 1], cache[row - 1][col])
    return cache[-1][-1]


# print(lcsRecursive(s1, s2, m, n))
print(lcsMemoizedRecursive(s1, s2, len(s2), len(s1), memo))
print(trverseSubstring(s2, memo))
print(np.array(lcsBottomsUp(s1, s2)))
