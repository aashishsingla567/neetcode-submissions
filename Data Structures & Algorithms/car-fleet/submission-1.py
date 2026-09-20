class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # pair and sort with positions
        pairs = []
        for i in range(n):
            p, s = position[i], speed[i]
            pairs.append((p, s, (target - p)/s))
        pairs.sort(key= lambda x: x[0])
        # print(pairs)

        stack = []

        for i in range(n - 1, -1, -1):
            p, s, t = pairs[i]
            # print(stack, (p, s, t))
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)