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

        for c in s:
            if c in oSet:
                stack.append(c)

            if c in cMap:
                if len(stack) == 0 or stack[-1] != cMap[c]:
                    return False
                stack.pop()

        if not stack:
            return True
        return False
