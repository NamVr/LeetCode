class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(mat), len(mat[0])

        rows = [sum(i) for i in mat]
        cols = [sum(i) for i in zip(*mat)]

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1 and rows[r] == 1 and cols[c] == 1: # check if they are special
                    res += 1

        return res
