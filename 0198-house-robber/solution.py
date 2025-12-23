class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0

        # a, b, i, i+1, ...
        for i in nums:
            temp = max(a+i, b)

            # update values for next iteration
            a = b
            b = temp
            # i is being incremented in the loop itself.
        
        return b
