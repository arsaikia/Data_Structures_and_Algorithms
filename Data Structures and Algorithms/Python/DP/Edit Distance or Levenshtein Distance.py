'''
72. Edit Distance   https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

---------------------------------------------------------------------------
Input: word1 = "horse", word2 = "ros"

Output: 3

Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
---------------------------------------------------------------------------

Example 2:

Input: word1 = "intention", word2 = "execution"

Output: 5

Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
---------------------------------------------------------------------------

'''

import numpy as np

word1 = "horse"
word2 = "ros"

# O(mn) Time | O(mn) Space
def editDistance(string1, string2):
    edits = [[i for i in range(len(string1) + 1)]
             for j in range(len(string2) + 1)]
    for row in range(1, len(edits)):
        edits[row][0] = 1 + edits[row - 1][0]

    for row in range(1, len(edits)):
        for col in range(1, len(edits[0])):
            if string1[col - 1] == string2[row - 1]:
                edits[row][col] = edits[row - 1][col - 1]
            else:
                edits[row][col] = 1 + min(edits[row - 1][col - 1],
                                          edits[row - 1][col],
                                          edits[row][col - 1])

    print(np.array(edits))
    return edits[-1][-1]


if __name__ == "__main__":
    print(editDistance(word1, word2))
