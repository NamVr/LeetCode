class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]

        if s.count('1') <= 1:
            return 0

        res = 0
        curr = 0

        for r in s:
            # base condition: if 1 is encountered
            
            if r == '0':
                curr += 1
            else:
                res = max(res, curr+1)
                curr = 0
        
        return res
