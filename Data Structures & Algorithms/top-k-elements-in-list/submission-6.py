from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = defaultdict(lambda: 0)

        for x in nums:
            freq[x] += 1

        for num, cnt in freq.items():
            buckets[cnt].append(num)
        
        ans = []

        for i in range(len(buckets) - 1, 0, -1):
            b = buckets[i]
            for ii in range(0, min(k - len(ans), len(b))):
                ans.append(b[ii])

        return ans

