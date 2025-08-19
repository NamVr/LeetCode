class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, curr = 0, 0

        for num in nums:
            # if num is 0, increment
            if num == 0:
                curr += 1
                res += curr

            # if num is not zero, reset
            else:
                curr = 0
        
        return res
