class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            return digits[0:-1] + [digits[-1] + 1]

        index = len(digits) - 1
        while digits[index] == 9:
            digits[index] = 0
            index -= 1
        if index < 0:
            digits.insert(0, 1)
        else:
            digits[index] += 1
        return digits
