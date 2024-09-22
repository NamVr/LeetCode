class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        i = 1

        def count(current):
            res = 0
            nei = current + 1
            while current <= n:
                res += min(nei, n + 1) - current
                current *= 10
                nei *= 10
            return res

        while i < k:
            steps = count(current)
            if i + steps <= k:
                current = current + 1
                i += steps
            else:
                current *= 10
                i += 1
        return current


