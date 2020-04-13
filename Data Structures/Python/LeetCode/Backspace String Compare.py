'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/

'''
from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if(len(S) != len(T)):
            return False

        S1 = S
        T1 = T

        i = 1
        x = len(S)
        while(i < x):
            if(S[i] == '#'):
                S = S.replace(S[i-1], '')
                i = min(1, i)
            else:
                i += 1
            x = len(S)

        i = 1
        x = len(T)
        while(i < x):
            if(T[i] == '#'):
                T = T.replace(T[i-1], '')
                i = min(1, i)
            else:
                i += 1
            x = len(T)
        return(S)


if __name__ == "__main__":
    sol = Solution()
    S = "xywrrmp"
    T = "xywrrmu#p"
    print(sol.backspaceCompare(S, T))
