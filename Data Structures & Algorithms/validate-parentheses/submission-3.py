oMap = {
    "{": "}",
    "[": "]",
    "(": ")",
}

cMap = {
    "}": "{",
    "]": "[",
    ")": "(",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] in oMap:
                stack.append(s[i])

            if s[i] in cMap:
                if len(stack) == 0 or stack[-1] != cMap[s[i]]:
                    return False
                stack.pop()
            i += 1

        if len(stack) == 0:
            return True
        return False
