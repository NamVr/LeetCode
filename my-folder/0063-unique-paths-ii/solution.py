class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * n
        if obstacleGrid[0][0] == 0: # space => possible to continue
            dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                # obstacle or not.
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        
        return dp[-1]
