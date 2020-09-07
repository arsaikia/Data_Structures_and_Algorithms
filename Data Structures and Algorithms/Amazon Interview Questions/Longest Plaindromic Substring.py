'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"

'''

string = 'abcd'


def longestPalindome(string):
    globalLongest = [0, 1]

    for i in range(len(string)):
        odd = getPalindrome(string, i - 1, i + 1)
        even = getPalindrome(string, i - 1, i)
        currLongest = max(odd, even, key=lambda x: x[1] - x[0])
        globalLongest = max(currLongest, globalLongest,
                            key=lambda x: x[1] - x[0])
    return string[globalLongest[0]: globalLongest[1]]


def getPalindrome(string, left, right):

    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break
    return [left + 1, right]


print(longestPalindome("aabacaxacddsdderf"))
