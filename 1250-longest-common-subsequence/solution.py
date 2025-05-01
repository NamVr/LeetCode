class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # 1. Get length of both texts
        m, n = len(text1), len(text2)

        # 2. Create DP table for n+1 X m+1 grid
        # fill all values with zero initially
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 3. bottom up DP approach, start with the last grid.
        for i in reversed(range(m)):
            for j in reversed(range(n)):

                # 4. Choice: If both text letter is same,
                # go diagonally up and add one.
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]

                # 5. Else, Take the max of cell below or left to you.
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        # 6. Return the maximum common subsequence at first cell.
        return dp[0][0]
