'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.
'''

from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        myStack = []
        starCount = 0

        for each in s:
            if( each == '('): myStack.append(each)
            elif (each == '*'): starCount += 1
            elif (each == ')' and len(myStack)!=0): myStack.pop()
        # if( len(myStack) != 0 and len(myStack) != starCount ): return False

        return starCount, myStack




if __name__ == "__main__":
    string1 = "(*))("
    sol = Solution()
    print(f'The Given string is a Valid Paranthesis ? : {sol.checkValidString(string1)}')