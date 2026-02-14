class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        l, r = 1, m * n

        while l < r:
            mi = (l + r) // 2
            if helper(mi):
                r = mi
            else:
                l = mi + 1
        return l
