class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Use BFS to track the shortest path.

        n = len(board)

        q = deque() # sq, moves
        q.append((1, 0)) # starting position

        visit = set() # to track already visited squares and not to revisit them in BFS.

        board.reverse() # easier calculations for position func()
        def pos(sq):
            r = (sq - 1) // n
            c = (sq - 1) % n

            # boustrophedon style check for even odd rows.
            # index wise, even rows are fine with above calculations
            # for odd sizes, reverse the array or subtract from N

            if r % 2: # odd check
                c = n-c-1

            return (r,c)
        
        # Start BFS.
        while q:
            # unpack the first element.
            sq, moves = q.popleft()
            
            # stimulate a dice throw
            for i in range(1,7):
                next_sq = sq + i # a dice throw adds up squares.

                # get cords of the new square.
                r,c = pos(next_sq)
                
                # check if there's a snake or a ladder.
                if board[r][c] != -1:
                    next_sq = board[r][c]
                
                # final base condition
                if next_sq == n*n:
                    return moves + 1
                
                # also check if already in visited hashset.
                if next_sq not in visit:
                    # traverse it if not visited.
                    visit.add(next_sq)
                    q.append((next_sq, moves + 1))

        return -1 # default edge case
