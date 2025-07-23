class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # 0 means water, that separates the islands
        # mark 0 when island is visited,
        # calculate total value and divisbility on the go

        res = 0
        N, M = len(grid), len(grid[0])

        def dfs(x, y):
            # Check for constraints.
            if x < 0 or y < 0 or x >= N or y >= M or grid[x][y] == 0:
                return 0

            # process total value and divisibility
            total = 0
            total += grid[x][y]
            grid[x][y] = 0

            # visit connected components
            for dx, dy in dirs:
                total += dfs(x + dx, y + dy)

            return total

        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    total = dfs(i, j)
                    if total % k == 0:
                        res += 1

        return res

