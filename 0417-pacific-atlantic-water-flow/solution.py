class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prev):
            """
            r - row index, c - column index
            visit - hashset (pac, atl)
            prev - previous height for bound checks.
            """

            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prev
            ):
                return

            # it is a new cell
            visit.add((r, c))

            # traverse all 4 boundaries.
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        pac, atl = set(), set()

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])

        # return res
        return list(pac.intersection(atl))
