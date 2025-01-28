class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            # check boundary conditions
            # check if land or already visited
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 0

            res = grid[r][c]
            grid[r][c] = 0 # marked as visited
            
            dirs = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in dirs:
                res += dfs(nr,nc)

            return res

        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    # if this is not in visited, explore the pond
                    res = max(res,dfs(r,c))
                
        return res
