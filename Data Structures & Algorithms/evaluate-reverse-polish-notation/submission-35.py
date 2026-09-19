def isnum(a: str):
    return a[-1].isdigit()

def op(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if a > 0 and b > 0:
                return a // b
            return int(a / b)

class Solution:
    # def op(self, a, b, op):
    #     if op == "+":
    #         return a + b
    #     if op == "-":
    #         return a - b
    #     if op == "*":
    #         return a * b
    #     if op == "/":
    #         if a > 0 and b > 0:
    #             return a // b
    #         return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        i = 0
        while i < n:
            if isnum(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(op(a, b, tokens[i]))
            i += 1
        return stack[0]