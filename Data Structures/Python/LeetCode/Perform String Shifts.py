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

        return shiftDict, shiftAmount, shiftDirection

if __name__ == "__main__":
    shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    s1 = [[1, 1], [0, 1]]
    s = "abcdefg"
    sol = Solution()
    print(sol.stringShift(s, shift))
