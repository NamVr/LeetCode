class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]

        # build the first row.
        for x in range(1,n):
            dp[x] = dp[x-1] + grid[0][x]

        for i in range(1,m):
            # for each row, the first column is different.
            dp[0] += grid[i][0]

            for j in range(1,n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
            
        
        return dp[-1]
