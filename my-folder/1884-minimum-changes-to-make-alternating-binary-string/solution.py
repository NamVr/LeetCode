class Solution:
    def minOperations(self, s: str) -> int:
        # test both ways
        # final string: 01010... or 101010...

        # min(count or n - count)

        res, n = 0, len(s)

        for i, c in enumerate(s): # i is index, c is character of string
            res += (ord(c) ^ i) & 1
        
        return min(res, n-res)

