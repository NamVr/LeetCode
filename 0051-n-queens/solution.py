class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # we will solve N Queen using 3 hashsets, row by row.
        col = set()
        pos = set() # r + c
        neg = set() # r - c

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # base condition, we reached last row.
            if r == n:
                # create a row copy so the main board is now affected.
                # they need a string copy for each row, not 2d array.
                row_copy = ["".join(row) for row in board]

                res.append(row_copy)
                return
            
            # recursive condition per row:
            for c in range(n):
                if c in col or (r + c) in pos or (r - c) in neg:
                    continue # no need if queen rule is violated.
                
                # it is a valid position, run backtrack.
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1) # to the next row

                # do cleanup for future backtracks.
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return res

