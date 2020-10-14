# O(n^2) Time | O(n) Space
def wordBreak(s, wordDict):
    words = set(wordDict)
    cache = {}
    getWordBreaks(s, words, 0, cache)
    # print(cache)
    if 0 in cache:
        return cache[0]
    return False


def getWordBreaks(string, words, idx, cache):
    if idx == len(string):
        return True
    if idx in cache:
        return cache[idx]

    hasWordBreaks = False

    for i in range(idx, len(string)):
        prefix = string[idx: i + 1]
        if prefix in words:
            hasWordBreaks = hasWordBreaks or getWordBreaks(string, words, i + 1, cache)
    cache[idx] = hasWordBreaks
    return cache[idx]

# O(n^2) Time | O(n) Space
def wordBreakBottomUp(string, wordDict):
    words = set(wordDict)
    cache = [False for _ in range(len(string) + 1)]
    cache[0] = True
    
    for i in range(1, len(cache)):
        for j in range(i):
            prefix = string[j : i]
            if cache[j] and prefix in words:
                cache[i] = True
    return cache[-1]


if __name__ == "__main__":
    s = "abcd"
    wordDict = ["a", "abc", "b", "cd"]
    print(wordBreak(s, wordDict) == wordBreakBottomUp(s, wordDict) )
