def wordBreak(s, wordDict):
    words = set(wordDict)
    cache = {}
    getWordBreaks(s, words, 0, cache)
    print(cache)
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


if __name__ == "__main__":
    s = "abcd"
    wordDict = ["a", "abc", "b", "cd"]
    print(wordBreak(s, wordDict))
