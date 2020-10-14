'''
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
'''


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:

        if string == "" or pattern == "":
            return False

        p = list(pattern)
        s = string.split(" ")
        if len(p) != len(s):
            return False

        cache = {}
        for i in range(len(p)):
            if p[i] not in cache and s[i] not in cache.values():
                cache[p[i]] = s[i]

        print(cache)
        for idx, each in enumerate(p):
            if each not in cache:
                return False
            if cache[each] != s[idx]:
                return False

        return True
