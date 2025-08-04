class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # find number of elements in the longest continuous sub array with exactly 2 distinct elements
        res = 0

        l, n = 0, len(fruits)
        s = defaultdict(int) # to check distinct elements

        for r in range(n):
            s[fruits[r]] += 1

            while len(s) > 2:
                s[fruits[l]] -= 1
                if s[fruits[l]] == 0:
                    del s[fruits[l]]
                l += 1

            res = max(res, r-l + 1)

        return res
