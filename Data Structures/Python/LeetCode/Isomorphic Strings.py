

'''
 Isomorphic Strings     https://leetcode.com/problems/isomorphic-strings/
 
 
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

'''


def repeatedSubstringPattern(s):
    start = 0
    end = len(string) - 1
    mid = (start+end) // 2

    midx = mid + 1
    while start <= mid and midx <= end:
        if string[start] != string[midx]:
            return False
            break
        else:
            start += 1
            midx += 1
    return True


string = "aba"

print(repeatedSubstringPattern(string))
