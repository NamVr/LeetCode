class Solution:
    MOD = 1337
    
    def pow(self, a:int, b: int) -> int:
        res = 1
        a %= self.MOD # overflow check

        while b > 0:
            # if odd, additional step.
            if b & 1:
                res = (res*a) % self.MOD
            
            a = (a*a) % self.MOD
            b >>= 1 # end step.

        return res     

    def superPow(self, a: int, b: List[int]) -> int:
        res = 1

        for i in reversed(range(len(b))):
            res = (res*self.pow(a,b[i])) % self.MOD
            a = self.pow(a,10)

        return res
