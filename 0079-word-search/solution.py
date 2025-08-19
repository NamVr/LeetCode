class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # During a search, you CAN NOT REVISIT same letter
        # So we will store a path variable that stores
        path = set() # (r,c) tuple stores the cords already visited.

        def dfs(r, c, i): # r,c cords and i is the index of word we're currently targetting.
            # Base Case: Stop if you have reached the last letter.
            if i == len(word):
                return True
            
            # Base Case: Return false IF
            # 1. Cords are out of bounds
            # 2. The word is revisited in the path
            # 3. Starting letter doesn't match the current search letter.
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in path or word[i] != board[r][c]:
                return False

            # Now we will do backtracking since the word is matched.
            # Visit all adjacent diagonals, if any condition satisfies, return true.
            # Mark the element visited, then explore, then cleanup.

            # 1. Mark the element visited.
            path.add((r,c))

            # 2. Visit all adjacent neighbours.
            res = (
                dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            )

            # 3. Cleanup.
            path.remove((r,c))

            # Return the result, at last.
            return res

        # We will now run the DFS on all grid elements.
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True # if any word search is found, return true immediately.
        
        # After all calls, no word is found.
        return False
