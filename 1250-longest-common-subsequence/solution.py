class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        # Create DP table for n+1 X m+1 grid
        # fill all values with zero initially
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # bottom up DP approach, start with the last grid.
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
