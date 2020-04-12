'''
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

        anagList = [] 
        opList=[]

        for each in strs:
            asciiVal = 1
            for ch in each:
                asciiVal += ord( ch )
            anagList.append( asciiVal )
        
        for i in range(len(anagList)):

        
        return anagList






if __name__ == "__main__":
    
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]

    anagramClass = Solution()

    print(anagramClass.groupAnagrams( input ))