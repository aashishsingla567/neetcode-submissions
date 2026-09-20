class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        i = n - 2
        stack = [n - 1]
        ans = [0] * n
        while i > -1:
            # print(i, stack, ans)
            while stack and temps[i] >= temps[stack[-1]]:
                stack.pop()
            top = stack[-1] if stack else i
            ans[i] = top - i
            stack.append(i)
            i -= 1
        return ans