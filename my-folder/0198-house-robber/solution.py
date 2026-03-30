class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # base cases
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        # now two variable approach DP
        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(a + nums[i], b)
            a, b = b, curr
        
        return b
