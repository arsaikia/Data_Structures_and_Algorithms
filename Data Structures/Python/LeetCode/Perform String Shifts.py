from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shiftDict = {0: 0,
                     1: 0}
        shiftAmount = 0
        shiftDirection = 0

        for each in shift:
            shiftDict[each[0]] += each[1]

        if(shiftDict[0] == shiftDict[1]):
            return s
        elif(shiftDict[0] > shiftDict[1]):
            shiftAmount = shiftDict[0] - shiftDict[1]
        else:
            shiftAmount = shiftDict[1] - shiftDict[0]
            shiftDirection = 1
        
        if(shiftAmount > len(s)):
            shiftAmount = shiftAmount % len(s)


        if( shiftDirection == 1 ):
            return shiftDict,shiftDirection,shiftAmount, s[(len(s)-shiftAmount):] + s[:(len(s)-shiftAmount)]
        else:
            return shiftDict,shiftDirection,shiftAmount, s[shiftAmount:] + s[:shiftAmount]


if __name__ == "__main__":
    shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    s = "abcdefg"

    shift1 = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    s1 = "xqgwkiqpif"


    
    sol = Solution()
    print(sol.stringShift("xqgwkiqpif", [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))
    # print('abcdefg'[4::1] + 'abcdefg'[:len(s)-3:1])
