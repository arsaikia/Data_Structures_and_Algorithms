'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"

'''

string = 'abcd'

op = []

for i in range(len(string)):
    for j in range(1, len(string)+1):
        op.append(string[i:j])
        
print(op)