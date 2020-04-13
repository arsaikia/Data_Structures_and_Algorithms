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

    def backspace(self, S):

        myList = []

        for each in S:
            if(each != '#'):
                myList.append(each)
            else:
                if(len(myList)): myList.pop()

        return (''.join(myList))


    def backspaceCompare(self, S: str, T: str) -> bool:

        return(self.backspace(S) == self.backspace(T))


if __name__ == "__main__":
    sol = Solution()
    S = "a#c"
    T = "b"
    print(sol.backspaceCompare(S, T))
