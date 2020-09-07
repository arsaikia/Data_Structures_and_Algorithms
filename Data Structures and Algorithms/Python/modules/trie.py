class Trie:
    def __init__(self, words):
        self.root = {}
        self.endSymbol = "*"
        for word in words:
            self.buildTrie(word)

    def buildTrie(self, word):
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        node[self.endSymbol] = True

    def searchWord(self, wordToSearch):
        node = self.root
        for char in wordToSearch:
            if char in node:
                node = node[char]
            else:
                return False
        return self.endSymbol in node

    def searchAll(self, wordToSearch):
        node = self.root
        for char in wordToSearch:
            if char in node:
                node = node[char]
        print(node, node.keys())
        return node if self.endSymbol not in node else []


if __name__ == "__main__":

    words = ["Apple", "Ant", "Animals", "Orange"]
    trie = Trie(words)

    print(trie.searchAll("A"))
