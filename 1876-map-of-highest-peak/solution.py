class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque([])
        ROWS, COLS = len(isWater), len(isWater[0])
        res = [[-1 for _ in range(COLS)] for _ in range(ROWS)] # -1 is unprocessed

        DIR = [0, 1, 0, -1, 0]

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    # this is water, default cell is 0
                    q.append((r,c))
                    res[r][c] = 0

        while q:
            r,c = q.popleft()

            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or res[nr][nc] != -1: continue
                res[nr][nc] = res[r][c] + 1
                q.append((nr,nc))
            

        return res
