class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # make a sliding window approach of 3 elements
        # first + third = 1/2 of second

        res = 0

        l, r = 0, 2

        while r < len(nums):
            # check condition
            if nums[l] + nums[r] == nums[l+1] / 2:
                res += 1
                
            # increment for next iteration
            l += 1
            r += 1

        return res
