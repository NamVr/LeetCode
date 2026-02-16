class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = (res << 1) | (n & 1) # from MSB, add it to res
            n >>= 1 # n chota ho rha hai

        return res
