class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
            res, sum = nums[0], nums[0]

            for i in range(1, len(nums)):
                # base condition for SI
                if nums[i] > nums[i-1]:
                    sum += nums[i]
                    res = max(res,sum)
                else:
                    sum = nums[i] # reset
            
            return res
