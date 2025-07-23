class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        # start with a bool array upto n
        sieve = [True] * n
        sieve[0] = sieve[1] = False

        # iterate from 2 .. n
        i = 2 
        while i*i < n: # upto sqrt
            if sieve[i]: # is true, maybe unmarked yet
                for j in range(i*i, n, i):
                    sieve[j] = False
            i += 1
        
        return sum(sieve)

