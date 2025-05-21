class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        N, M = len(matrix), len(matrix[0])

        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 0: # set this to 0s.
                    row.add(r)
                    col.add(c)
        
        # Modify in-place for Rows.
        for r in row:
            for c in range(M):
                matrix[r][c] = 0
        
        for c in col:
            for r in range(N):
                matrix[r][c] = 0
                
