class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Build the graph. char -> neighbor characters
        adjMap = {ch: set() for word in words
                  for ch in word}

        for idx in range(len(words) - 1):
            wordOne = words[idx]
            wordTwo = words[idx + 1]

            commonSeq = min(len(wordOne), len(wordTwo))

            # Edge case:
            # if commonSeq is same in wordOne and wordTwo
            # but wordTwo has more characters, return " "
            if len(wordOne) > len(wordTwo) and wordOne[: commonSeq] == wordTwo[: commonSeq]:
                return ""

            # iterate over common seq until we find a distinct character
            for j in range(commonSeq):
                # find the first distinct char and add to graph
                if wordOne[j] != wordTwo[j]:
                    src, dst = wordOne[j], wordTwo[j]
                    adjMap[src].add(dst)
                    break

        # variables to keep track of visited node, cycles and store results
        visited, visiting, charOrder = set(), set(), []

        # traverse each character and do postorderDfs to find topoloical order
        for node in adjMap:
            foundCycle = self.topologicalSortUsingPostorderDFS(
                node, adjMap, visited, visiting, charOrder)
            if foundCycle:
                return ""

        return "".join(reversed(charOrder))

    # returns true if found a cycle, updates result without returning
    def topologicalSortUsingPostorderDFS(self, node, adjMap, visited, visiting, charOrder):
        if node in visiting:
            return True
        if node in visited:
            return False

        visiting.add(node)
        visited.add(node)

        for nextNode in adjMap[node]:
            if self.topologicalSortUsingPostorderDFS(nextNode, adjMap, visited, visiting, charOrder):
                return True

        charOrder.append(node)
        visiting.remove(node)
        return False
