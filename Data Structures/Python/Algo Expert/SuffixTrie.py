class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.buildTrieStartingAt(i, string)
    
    def buildTrieStartingAt(self, idx, string):
        pass

    def contains(self, string):
        node = root
        for i in range(len(string)):
            currLetter = string[i]
            if currLetter in node:
                node = node[currLetter]
            else:
                return False
        return self.endSymbol in node
    
    
    
if __name__ == "__main__":
    pass