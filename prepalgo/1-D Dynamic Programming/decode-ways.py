# TOP-DOWN (RECURSIVE)
# O(N) Time | O(N) Space
class Solution:
    def canHaveValidDoubleDigitsChar(self, idx, string):
            idxInBounds = idx + 1 < len(string)
            if not idxInBounds:
                return False

            startsWithOne = string[idx] == "1"
            startsWithTwoAndHasValidSecondDigits = string[idx] == "2" and string[idx + 1] in "0123456"
            if startsWithOne or startsWithTwoAndHasValidSecondDigits:
                return True
            return False
    
    def traverse(self, s, i):
            if i in self.ways:
                return self.ways[i]
            if s[i] == "0":
                return 0
            
            res = self.traverse(s, i + 1)

            if self.canHaveValidDoubleDigitsChar(i, s):
                res += self.traverse(s, i + 2)
            
            self.ways[i] = res
            return self.ways[i]
    
    def numDecodings(self, s: str) -> int:
        self.ways = { len(s) : 1 }        
        return self.traverse(s, 0)

######################################################################
# Bottom UP
# O(N) Time | O(N) Space
class Solution:
    def canHaveValidDoubleDigitsChar(self, idx, string):
            idxInBounds = idx + 1 < len(string)
            if not idxInBounds:
                return False

            startsWithOne = string[idx] == "1"
            startsWithTwoAndHasValidSecondDigits = string[idx] == "2" and string[idx + 1] in "0123456"
            if startsWithOne or startsWithTwoAndHasValidSecondDigits:
                return True
            return False
    
    def numDecodings(self, s: str) -> int:
        self.ways = { len(s) : 1 }   
        
        for idx in reversed(range(len(s))):
            if s[idx] == "0":
                self.ways[idx] = 0
            else:
                self.ways[idx] = self.ways[idx + 1]

                if self.canHaveValidDoubleDigitsChar(idx, s):
                    self.ways[idx] += self.ways[idx + 2]
        
        return self.ways[0]

######################################################################

