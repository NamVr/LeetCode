class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 free
        # 1 guardable
        # 2 guard
        # 3 wall
        grid = [[0] * n for _ in range(m)]

        for r,c in guards:
            grid[r][c] = 2
        
        for r,c in walls:
            grid[r][c] = 3

        def helper(r,c):
            # all 4 directions
            for row in range(r+1, m):
                if (grid[row][c] > 1):
                    break
                grid[row][c] = 1
            
            for row in reversed(range(0, r)):
                if (grid[row][c] > 1):
                    break
                grid[row][c] = 1

            for col in range(c+1, n):
                if (grid[r][col] > 1):
                    break
                grid[r][col] = 1
            
            for col in reversed(range(0, c)):
                if (grid[r][col] > 1):
                    break
                grid[r][col] = 1
        
        for r,c in guards:
            helper(r,c)
        
        res = 0

        for row in grid:
            for r in row:
                if not r:
                    res+=1

        return res

