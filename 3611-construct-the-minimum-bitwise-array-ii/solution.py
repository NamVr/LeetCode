class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N

        for i in range(N):
            if nums[i] == 2:
                continue # edge case, 2 is the only even prime
            
            n = nums[i]
            pos = 0

            while n > 0 and (n >> pos) & 1 == 1:
                pos += 1 # right shift till a zero is found
            
            if (1 << pos) > n:
                highestBit = n.bit_length() - 1
                n = n & ~(1 << highestBit)
            else:
                n = n & ~(1 << (pos - 1))
            
            res[i] = n

        return res
