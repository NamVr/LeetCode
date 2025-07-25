class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()

        if nums[-1] <= 0:
            return nums[-1]

        res = 0
        
        nums = set(nums)
        for num in nums:
            if num > 0:
                res += num
        
        return res
