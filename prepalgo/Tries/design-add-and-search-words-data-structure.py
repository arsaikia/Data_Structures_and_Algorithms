class WordDictionary:

    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    # O(N) Time | O(N) Space
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = {}

    def search(self, word: str) -> bool:

        def dfs(node, startingIdx):

            for idx in range(startingIdx, len(word)):
                char = word[idx]
                if char == ".":
                    for nextNode in node.values():
                        if dfs(nextNode, idx + 1):
                            return True
                    return False
                else:
                    if char not in node:
                        return False
                    node = node[char]

            return self.endSymbol in node

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("bad")
# param_2 = obj.search("bad")
