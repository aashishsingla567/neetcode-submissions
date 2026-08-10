class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        sufixes = [0] * len(nums)

        prefixes[0] = nums[0]
        sufixes[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            sufixes[i] = sufixes[i + 1] * nums[i]

        res = [0] * len(nums)
        res[0] = sufixes[1]
        res[-1] = prefixes[-2]

        for i in range(1, len(nums) - 1):
            res[i] = prefixes[i - 1] * sufixes[i + 1]
        
        return res