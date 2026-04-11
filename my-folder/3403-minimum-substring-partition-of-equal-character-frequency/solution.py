class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [0] + [n]*n

        for i in range(n):
            count = defaultdict(int)

            for j in range(i, n):
                count[s[j]] += 1

                if len(set(count.values())) == 1: # balanced condition
                    dp[j+1] = min(dp[j+1], dp[i] + 1)

        return dp[-1]
