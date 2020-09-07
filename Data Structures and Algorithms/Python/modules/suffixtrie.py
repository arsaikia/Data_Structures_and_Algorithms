class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTree(string)

    def populateSuffixTree(self, string):
        tree = self.root
        for i in range(len(string)):
            self.buildTreeFromIndex(i, string)

    def buildTreeFromIndex(self, idx, string):
        tree = self.root
        for i in range(idx, len(string)):
            letter = string[i]
            if letter not in tree:
                tree[letter] = {}
            tree = tree[letter]
        tree[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


if __name__ == "__main__":
    trie = SuffixTrie("apple")
    print(trie.root)
