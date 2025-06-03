class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # 0 to N.
        rows = defaultdict(set)
        boxs = defaultdict(set) # (x // 3)

        # r 0 -> 2 (box = 0,1,2)
        # r 3 -> 5 (box = 3,4,5)
        # r 6 -> 8 (box = 6,7,8)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxs[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxs[(r // 3, c // 3)].add(board[r][c])
        
        return True
