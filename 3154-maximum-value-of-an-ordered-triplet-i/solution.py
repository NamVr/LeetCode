class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res,n = 0, len(nums)
        left = nums[0] # initially
        
        for j in range(1, n):
            # add max greedy approach
            if left < nums[j]:
                # update max value
                left = nums[j]
                continue

            for k in range(j+1, n):
                res = max(res, (left - nums[j]) * nums[k])

        return res
