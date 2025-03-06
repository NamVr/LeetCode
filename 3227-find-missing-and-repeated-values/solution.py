class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set() # set of numbers
        n = len(grid)
        a = 0
        b = (1 + n*n) * n*n // 2

        # first number is 1, last number is n^2
        # (first + last) * n // 2

        for i in range(n):
            for j in range(n):
                x = grid[i][j]

                # check if this number exits in our set
                if x in s:
                    a = x
                else:
                    s.add(x)
                    b -= x
        
        return [a,b]
