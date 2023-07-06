class Solution:
    # O(N*K) Time | O(N*K) Space => N -> Number of words; K -> Max Word Length
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        result = []

        for word in strs:
            charCount = [0 for __ in range(26)]
            for char in word:
                charIdx = ord(char) - ord("a")
                charCount[charIdx] += 1
            anagrams[tuple(charCount)].append(word)

        for anagramGroup in anagrams.values():
            result.append(anagramGroup)

        return result
