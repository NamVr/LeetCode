class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        max_val = max(nums)
        maxs = []

        for i, x in enumerate(nums):
            if x == max_val:
                maxs.append(i)
            
            freq = len(maxs)
            if freq >= k:
                res += 1 + maxs[-k]
        return res
