class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(x):
            stores = 0

            for q in quantities:
                stores += math.ceil(q/x)
            
            return stores <= n

        l, r = 1, max(quantities)
        res = 0

        while (l <= r):
            m = l + (r-l)//2
            if (helper(m)):
                res = m
                r = m-1
            else:
                l = m+1

        return res
