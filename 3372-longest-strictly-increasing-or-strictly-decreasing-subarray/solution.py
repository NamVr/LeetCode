class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = res = 1

        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                # next number is larger, SI sequence
                inc += 1
                dec = 1 # reset
            elif nums[i+1] < nums[i]:
                dec += 1
                inc = 1
            else:
                # reset both counters
                inc = dec = 1
            
            # lastly, update result for each iteration
            res = max(res, inc, dec)

        return res
