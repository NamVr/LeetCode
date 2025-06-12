class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = float("-inf") # to get the maximum value, take the minimum value.
        n = len(nums)

        for i in range(1,n): # 1 to last value.
            res = max(res, abs(nums[i] - nums[i-1]))
        
        # last check for the circular array, last and the first element.
        res = max(res, abs(nums[0]-nums[n-1]))

        return res
