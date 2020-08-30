
def LCS(s1, s2, m, n, memo):

    if m < 0 or n < 0:
        return 0

    if memo[m][n] is not None:
        # print("\nHERE", memo)
        return memo[m][n]
    else:
        if s1[m-1] == s2[n-1]:
            result = 1 + LCS(s1, s2, m-1, n-1, memo)
        else:
            result = max(LCS(s1, s2, m-1, n, memo), LCS(s1, s2, m, n-1, memo))
    memo[m][n] = result
    return result


def longestCommonSubsequence(str1, str2):
    lcs = [[[] for col in range(len(str1)+1)] for row in range(len(str2)+1)]

    for row in range(1, len(lcs)):
        for col in range(1, len(lcs[0])):
            if str2[row-1] == str1[col-1]:
                lcs[row][col] = lcs[row - 1][col - 1] + [str2[row - 1]]
            else:
                lcs[row][col] = max(lcs[row-1][col], lcs[row][col-1], key=len)
    return ''.join(lcs[-1][-1])


string1 = 'BATD'
string2 = 'ABACD'
memo = [[None for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]
# print(memo)
print(LCS(string1, string2, len(string1)-1, len(string2)-1, memo))

print(longestCommonSubsequence(string1, string2))
