class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        res = nums[0] #guaranteed 1 solution

        for i in nums:
            if curr < 0:
                curr = 0
            curr += i

            res = max(res,curr)
        
        return res
