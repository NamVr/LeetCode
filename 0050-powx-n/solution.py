class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = 1
        b = abs(n) # in form of a ^ b
        # x = x % MOD

        while b: # b > 0
            if b & 1: # b is odd, additional step.
                res *= x # res = (res*x) % MOD
            x *= x # x = (x*x) % MOD

            b >>= 1 # end step.

        return res if n >= 0 else 1 / res
