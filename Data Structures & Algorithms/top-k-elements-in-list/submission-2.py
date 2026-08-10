from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(lambda: 0)
        for x in nums:
            freqs[x] += 1
            
        freq_arr = list(freqs.items())

        sorted_freq_arr = sorted(freq_arr, key=lambda x:-x[1])

        ans = []
        for i in range(k):
            ans.append(sorted_freq_arr[i][0])
        return ans

