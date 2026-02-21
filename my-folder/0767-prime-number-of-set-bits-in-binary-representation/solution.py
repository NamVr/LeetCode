class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        N = 22
        sieve = [True] * N
        sieve[0] = sieve[1] = False

        i = 2
        while i*i < N:
            if sieve[i] < N:
                for j in range(i*i, N, i):
                    sieve[j] = False
            i += 1
        
        res = 0

        for i in range(left, right+1):
            #if sieve[bin(i)[2:].count('1')]:
            if sieve[i.bit_count()]:
                res += 1

        return res
