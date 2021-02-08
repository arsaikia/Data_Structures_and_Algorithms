'''
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example
ABCE
SFCS
ADEE

Input: board =
[
    ["A", "B", "C", "E"],
    ["B", "F", "C", "S"],
    ["A", "D", "E", "E"]
],
word = "ABCCED"
Output: true
'''


def findWord(board, word):
    visited = [[False for col in row] for row in board]

    letterIdx = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if visited[row][col]:
                continue

            if word[letterIdx] != board[row][col]:
                continue

            found = traverseNode(row, col, visited, board,  word, letterIdx)
            if found:
                return True
    return False


def traverseNode(row, col, visited, board, word, idx):
    stack = [[row, col]]

    while len(stack):
        if idx == len(word) - 1:
            return True
        node = stack.pop()
        i, j = node[0], node[1]
        visited[i][j] = True
        neighbors = findMatchingNeighbors(i, j, board, word, idx, visited)
        if len(neighbors):
            idx += 1
        for neighbor in neighbors:
            stack.append(neighbor)
        visited[i][j] = False

    return False


def findMatchingNeighbors(i, j, board, word, idx, visited):
    nextLetter = word[idx + 1]

    neighbors = []

    if i > 0 and not visited[i - 1][j] and board[i - 1][j] == nextLetter:
        neighbors.append([i-1, j])

    #
    #
    #

    return neighbors
