'''
🎈🎈
Given an array of strings, group anagrams together.

__Example:__
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
__Note:__

*  All inputs will be in lowercase.
*  The order of your output does not matter.

'''

from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagDict = {}

        for each in strs:
            x = self.primeHash(each)
            if anagDict.get(str(x)):
                anagDict[str(x)].append(each)
            else:
                anagDict[str(x)] = [each]

        return [anagDict[i] for i in anagDict.keys()]

    def primeHash(self, str: str) -> int:
        primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        x = 1
        for ch in str:
            x *= primeList[ord(ch)-97]
        return x
    
## MUCH FASTER
    def groupAnagrams_intuitive(self, words: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in words:
            wordSorted = "".join(sorted(word))
            if wordSorted in anagrams:
                anagrams[wordSorted].append(word)
            else:
                anagrams[wordSorted] = [word]
        return list(anagrams.values())


if __name__ == "__main__":
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]

    anagramClass = Solution()
    print(anagramClass.groupAnagrams(input))
    print(anagramClass.groupAnagrams_intuitive(input))
    