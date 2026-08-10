class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            front, back = nums[i], nums[j]
            if front + back == target:
                return [i + 1, j + 1]
            if front + back > target:
                j -= 1
            else:
                i += 1
        
        # it should never reach here
        return []
