class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]

        dirs = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]

        for r in range(m):
            for c in range(n):

                # if already visited.
                if visited[r][c]:
                    continue # skip the loop

                # stack for current letter. row, col, parent_row, parent_col
                stack = [(r, c, -1, -1)] 

                # mark this letter and cell visited.
                visited[r][c] = True

                while stack:
                    cr, cc, pr, pc = stack.pop()

                    # explore all 4 boundaries
                    for dr, dc in dirs:
                        nr, nc = dr + cr, dc + cc

                        # base case.
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue # out of bounds.
                        
                        if grid[nr][nc] != grid[cr][cc]:
                            continue # not the same letter, visit in another cycle.
                        
                        if nr == pr and nc == pc:
                            continue # don't go back to parent
                        
                        # finally, if it is marked visited in same cycle
                        if visited[nr][nc]:
                            return True
                        
                        visited[nr][nc] = True
                        stack.append((nr, nc, cr, cc))

        return False
