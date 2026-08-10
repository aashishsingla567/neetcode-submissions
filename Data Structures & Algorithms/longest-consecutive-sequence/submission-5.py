from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for n in nums:
            if n - 1 in s:
                continue
            nn = n
            seq_len = 0
            while nn in s:
                print(nn)
                seq_len += 1
                nn += 1
            max_len = max(max_len, seq_len)
        return max_len
