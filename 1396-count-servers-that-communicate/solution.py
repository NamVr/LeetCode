class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0

        n, m = len(grid), len(grid[0])
        rows = [0] * n
        cols = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j]: # is 1
                    rows[i] += 1
                    cols[j] += 1

        for i in range(n):
            for j in range(m):
                # main check condition to remove duplicacy:
                if (grid[i][j] and (rows[i] > 1 or cols[j] > 1)):
                    # if grid is 1 and if row or column counter has more than 1 servers
                    res += 1

        return res
