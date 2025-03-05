class Solution:
    def coloredCells(self, n: int) -> int:
        # at every increment, difference is of 4
        # 1 2 3  4  5
        # 1 5 13 25 41

        # for n steps, 1 + (4x1) + (4x2) + .. + (4x(n-1))
        # n = 1 + 4 (1 + 2 + 3 + ... + (n-1))
        # n = 1 + 4 (Sum of series)
        # 9 8 7 6 5 ... 1
        # 1 2 3 4 5 ... 9) if n = 10
        # 10 * 9 / 2 or simply N * (N-1) / 2

        # n = 1 + 4 (N*(N-1)/2) = 1 + 2(N * (N-1))

        return 1 + 2 * n * (n-1)
