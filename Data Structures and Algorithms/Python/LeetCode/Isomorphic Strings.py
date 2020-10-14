

'''
 Isomorphic Strings     https://leetcode.com/problems/isomorphic-strings/
 
 
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

'''


def isIsomorphic(s, t):
    visited = {}
    for i in range(len(s)):
        if s[i] not in visited:
            if t[i] in visited.values():
                return False
            visited[s[i]] = t[i]

        else:
            if visited[s[i]] != t[i]:
                return False
    return True


s = "egg"
t = "add"
print(isIsomorphic(s, t))
