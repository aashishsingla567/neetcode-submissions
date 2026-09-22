import math


class Solution:
    def calcTime(self, piles, k):
        time = 0
        for b in piles:
            time += math.ceil(b / k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        ans = maxPile

        while l <= r:
            mid = int((l + r) / 2)
            time = self.calcTime(piles, mid)
            # print(l, r, mid, time)
            if time <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
