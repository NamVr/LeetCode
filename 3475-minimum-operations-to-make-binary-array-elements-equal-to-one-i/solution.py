class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                # perform a flip
                res += 1
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
            
        if not nums[-1] or not nums[-2]:
            return -1

        return res
