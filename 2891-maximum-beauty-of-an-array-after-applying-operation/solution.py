class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, res = 0, 0

        for right in range(len(nums)):
            while nums[right]-nums[left] > 2*k:
                left += 1
            
            res = max(res, right-left+1)
        
        return res
