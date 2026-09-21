class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stack of (index, height)
        ans = 0
        for i, h in enumerate(heights):
            start = i
            # print(i, h, stack, ans)
            while stack and stack[-1][1] >= h:
                t_i, t_h = stack.pop()
                # print(t_i, t_h, h)
                area = t_h * (i - t_i)
                # print(area)
                ans = max(ans, area)
                start = t_i # needed for next appends
            # start will either be current index or index of last poped(larger than current) bar
            # pushed element is larger than current top
            stack.append((start, h))

        n = len(heights)
        for i, h in stack:
            # print(i, h, stack, ans)
            area = h * (n - i)
            ans = max(ans, area)

        return ans
