class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # store sums of both rows (first and second)
        first = sum(grid[0])
        second = 0

        # set result to a very high value
        res = float("inf")

        # iterate through the first row grid
        for i in range(len(grid[0])):
            # subtract each first row element from first sum
            first -= grid[0][i]

            # find the minimum of current result or the maximum of first or second row sum
            res = min(res, max(first,second))

            # finally add the second row
            second += grid[1][i]
        
        return res
