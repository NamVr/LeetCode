class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]] # all 4 directions

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return # if water or out of bounds, do nothing
            
            # mark is as visited.
            grid[r][c] = "0"

            # run DFS for all neighbors
            for nr, nc in dirs:
                dfs(r + nr, c + nc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c) # run dfs if this is land
                    res += 1
        
        return res
