import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        ans = maxPile

        while l <= r:
            mid = (l + r) // 2
            
            time = 0
            for b in piles:
                time += math.ceil(b / mid)
            
            # print(l, r, mid, time)
            if time <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
