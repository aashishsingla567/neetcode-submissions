oSet = {
    "{",
    "[",
    "(",
}

cMap = {
    "}": "{",
    "]": "[",
    ")": "(",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in oSet:
                stack.append(s[i])

            if s[i] in cMap:
                if len(stack) == 0 or stack[-1] != cMap[s[i]]:
                    return False
                stack.pop()
            i += 1

        if len(stack) == 0:
            return True
        return False
