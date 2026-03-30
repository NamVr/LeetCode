class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1 # start from 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: # if obstacle
                    grid[i][j] = 0 # make it unreachable
                else:
                    if i > 0: # only if left column exists
                        grid[i][j] += grid[i-1][j]
                    if j > 0: # only if upper row exists
                        grid[i][j] += grid[i][j-1]
        
        return grid[-1][-1]
