class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, prefix, postfix = len(nums), 1, 1
        res = [1] * n

        # two loops, prefix and suffix.
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in reversed(range(n)):
            res[i] *= postfix
            postfix *= nums[i]

        return res
