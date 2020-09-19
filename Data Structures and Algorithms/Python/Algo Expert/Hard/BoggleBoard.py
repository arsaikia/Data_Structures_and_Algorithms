#----------------------------< BOGGLE BOARD >-------------------------------

# O(ws +nm * 8^s) || O(nm + ws) Space
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for col in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            traverseNode(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def traverseNode(row, col, board, trieNode, visited, finalWords):
    if visited[row][col]:
        return
    letter = board[row][col]
    if letter not in trieNode:
        return
    visited[row][col] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(row, col, board)
    for neighbor in neighbors:
        traverseNode(neighbor[0], neighbor[1], board,
                     trieNode, visited, finalWords)
    visited[row][col] = False


def getNeighbors(i, j, board):
    neighbors = []

    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i + 1, j - 1])
    if i > 0:
        neighbors.append([i - 1, j])
    if i < len(board) - 1:
        neighbors.append([i + 1, j])
    if j > 0:
        neighbors.append([i, j - 1])
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    # O(s) Time , s : Characters in a word | O(s) Space
    def add(self, word):
        node = self.root
        for letter in word:
            if letter in node:
                node = node[letter]
            else:
                node[letter] = {}
                node = node[letter]
        node[self.endSymbol] = word


if __name__ == "__main__":
    board = [
        ["t", "h", "i", "s", "i", "s", "a"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"]
    ]
    words = [
        "this",
        "is",
        "not",
        "a",
        "simple",
        "boggle",
        "board",
        "test",
        "REPEATED",
        "NOTRE-PEATED"
    ]
    print(boggleBoard(board, words))

