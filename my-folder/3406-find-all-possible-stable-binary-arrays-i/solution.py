class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[-1]*2 for _ in range(201)] for _ in range(201)]

        def solve(z, o, last):
            if z == zero and o == one:
                return 1

            if dp[z][o][last] != -1:
                return dp[z][o][last]

            res = 0

            if last == 0:
                for k in range(1, limit + 1):
                    if o + k > one: break
                    res = (res + solve(z, o + k, 1)) % MOD
            else:
                for k in range(1, limit + 1):
                    if z + k > zero: break
                    res = (res + solve(z + k, o, 0)) % MOD

            dp[z][o][last] = res
            return res

        res = 0

        for k in range(1, min(limit, zero) + 1):
            res = (res + solve(k, 0, 0)) % MOD

        for k in range(1, min(limit, one) + 1):
            res = (res + solve(0, k, 1)) % MOD

        return res
