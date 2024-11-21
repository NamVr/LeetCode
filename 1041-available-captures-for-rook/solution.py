class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # grid given with p = black pawn, B = white bishop and R only 1 as main rook. all other are "." empty
        # approach: find the rook then calculate in all 4 directions
        m = len(board)
        n = len(board[0])

        def helper(r,c):
            res = 0
            # simulate all 4 directions
            for row in range(r+1, m):
                if board[row][c] != ".":
                    if board[row][c] == "p":
                        res += 1
                    break
                
            for row in reversed(range(0,r)):
                if board[row][c] != ".":
                    if board[row][c] == "p":
                        res += 1
                    break

            for col in range(c+1, n):
                if board[r][col] != ".":
                    if board[r][col] == "p":
                        res += 1
                    break

            for col in reversed(range(0,c)):
                if board[r][col] != ".":
                    if board[r][col] == "p":
                        res += 1
                    break
            
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == "R":
                    return helper(r,c)
