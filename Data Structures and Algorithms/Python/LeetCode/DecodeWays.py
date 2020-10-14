class Solution:
    def __init__(self):
        self.memo = {}

    def numDecodings(self, string: str) -> int:
        if string[0] == '0':
            return 0
        return self.decodeWaysBottomsUp(string, 0, self.memo)

    def decodeWaysBottomsUp(self, string, idx, memo):

        if idx == len(string):
            return 1

        if string[idx] == '0':
            return 0

        if idx == len(string) - 1:
            return 1
        if idx in memo:
            return memo[idx]

        memo[idx] = self.decodeWaysBottomsUp(string, idx + 1, memo) + \
            (self.decodeWaysBottomsUp(string, idx + 2, memo)
             if int(string[idx: idx + 2]) <= 26 else 0)

        return memo[idx]





def decodeWaysBottomsUp(string):
    
    if not len(string):
        return 0
    if string[0] == '0':
        return 0
    
    cache = [0 for __ in range(len(string) + 1)]
    cache[0] = 1
    cache[1] = 0 if string[0] == '0' else 1
    
    for i in range(2, len(string) + 1):

        if string[i - 1] != '0':
            cache[i] += cache[i - 1]
            
        twoDigits = int(string[i-2 : i])
        if 10 <= twoDigits <= 26:
            cache[i] += cache[i - 2]
    return cache[-1]


print(decodeWaysBottomsUp('10'))
