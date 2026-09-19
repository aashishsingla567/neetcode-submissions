def isnum(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

class Solution:
    def op(self, a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a / b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
        
            while isnum(tokens[i]):
                stack.append(int(tokens[i]))
                i += 1
                if i == len(tokens):
                    return stack.pop()
            op = tokens[i]
            b, a = stack.pop(), stack.pop()
            out = self.op(a, b, op)
            stack.append(int(out))
        
            i += 1
        
        return stack.pop()