from pprint import pprint as pprint


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) Time | O(n^2) Space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.buildTrieStartingAt(i, string)

    def buildTrieStartingAt(self, idx, string):
        node = self.root
        for j in range(idx, len(string)):
            if string[j] not in node:
                node[string[j]] = {}
            node = node[string[j]]
        node[self.endSymbol] = True

    # O(m) Time | O(1) Space
    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            currLetter = string[i]
            if currLetter in node:
                node = node[currLetter]
            else:
                return False
        return self.endSymbol in node


if __name__ == "__main__":
    ST = SuffixTrie("APPLE")
    print(ST.contains("APPLE"))

    pprint(ST.root, width=1)
