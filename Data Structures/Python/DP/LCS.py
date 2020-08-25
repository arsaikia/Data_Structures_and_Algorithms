
def LCS(s1, s2, m, n, memo):
    
    if m < 0 or n < 0:
        return 0
    
    if memo[m][n] is not None:
        print("HERE", m, n)
        return memo[m][n]
    else:
        if s1[m-1] == s2[n-1]:
            result = 1 + LCS(s1, s2, m-1, n-1, memo)
        else:
            result = max(LCS(s1, s2, m-1, n, memo), LCS(s1, s2, m, n-1, memo))
    memo[m][n] = result
    return result


string1 = 'BATD'
string2 = 'ABACD'
memo = [[None for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]
# print(memo)
print(LCS(string1, string2, len(string1)-1, len(string2)-1, memo))
