class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])

        res = [[1] * m for _ in range(n)]

        # i is i // m
        # j is j % m

        # two pass solution.
        # Pass 1: Prefix
        for idx in range(1, n*m):
            i = idx // m
            j = idx % m

            pi, pj = (idx-1) // m, (idx-1) % m

            res[i][j] = res[pi][pj] * grid[pi][pj] % MOD
        
        # Pass 2: Suffix
        suffix = 1
        for idx in reversed(range(n*m)):
            i, j = idx // m, idx % m

            res[i][j] = suffix * res[i][j] % MOD
            suffix = suffix * grid[i][j] % MOD
        
        return res
