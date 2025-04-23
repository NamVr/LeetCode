class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we will compare overall result and current result,
        # keep max() at every island, explore in 4 dirs.
        # mark island as visited by turning 1s to 0s.
        res = 0
        M, N = len(grid), len(grid[0])

        def dfs(r, c): # returns current area.

            # base condition: check boundary conditions or if it is water.
            if r < 0 or r >= M or c < 0 or c >= N or grid[r][c] == 0:
                return 0

            # run island spanning tests here, (r,c) is a island, add 1.
            grid[r][c] = 0 # mark as visited.
            area = 1
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            
            # now we know, it is in bounds and is a land piece.
            # expand to the borders using dfs.

            for dr, dc in dirs:
                area += dfs(dr, dc)
            
            # after all execution, return total area of this island.
            return area
        
        # call dfs at every 1, iterate for all combinations.
        for m in range(M):
            for n in range(N):
                
                # if 1, its a new island, explore using dfs.
                if grid[m][n] == 1:
                    res = max(res, dfs(m,n))
                
                # if its not 1, do nothing, reset cur.
                
        return res
