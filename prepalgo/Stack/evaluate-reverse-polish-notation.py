# O(N) Time
# O(N) Space
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ADDITION, SUBTRACTION, DIVISION, MULTIPLICATION = "+", "-", "/", "*"
        operations = set([ADDITION, SUBTRACTION, DIVISION, MULTIPLICATION])
        stack = []

        for token in tokens:

            if token not in operations:
                stack.append(int(token))
                continue

            one = stack.pop()
            two = stack.pop()
            
            if token == ADDITION:
                res = one + two
            elif token == SUBTRACTION:
                res = two - one
            elif token == DIVISION:
                res = int(float(two) / one)
            elif token == MULTIPLICATION:
                res = one * two
            stack.append(int(res))
        return stack[0]