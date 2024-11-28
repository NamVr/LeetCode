class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque([(0,0,0)]) # obstracle count, r, c
        visit = set([(0,0)]) # cordinates

        # O(nm)

        while q:
            obs, r, c = q.popleft()

            # if we reach target, return
            if (r,c) == (ROWS-1, COLS-1):
                return obs
            
            nei = [ # neighbours
                [r + 1, c],
                [r - 1, c],
                [r, c + 1],
                [r, c - 1]
            ]

            for nr, nc in nei:
                # if visited OR not in bounds:
                if (nr, nc) in visit or nr < 0 or nc < 0 or nc == COLS or nr == ROWS:
                    continue
                
                # explore it
                if grid[nr][nc]:
                    q.append((obs+1, nr, nc))
                else:
                    q.appendleft((obs, nr, nc))
                visit.add((nr,nc))
