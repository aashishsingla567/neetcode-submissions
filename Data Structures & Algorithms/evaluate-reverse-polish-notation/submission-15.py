def isnum(a: str):
    return a[-1].isdigit()

class Solution:
    def op(self, a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        n = len(tokens)
        while i < n:
            while isnum(tokens[i]):
                stack.append(int(tokens[i]))
                i += 1
                if i == n:
                    return stack.pop()
            b = stack.pop()
            a = stack.pop()
            stack.append(self.op(a, b, tokens[i]))
            i += 1
        return stack.pop()