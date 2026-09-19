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
        for t in tokens:
            if isnum(t):
                stack.append(int(t))
                continue
            b = stack.pop()
            a = stack.pop()
            stack.append(self.op(a, b, t))
        return stack.pop()