class Solution:
    def solveQueries(self, nums, queries):
        m = defaultdict(list)
        n = len(nums)

        # store indices
        for i, x in enumerate(nums):
            m[x].append(i)

        res = []

        for i in queries:
            val = nums[i]
            positions = m[val]

            if len(positions) == 1:
                res.append(-1)
                continue

            pos = bisect_left(positions, i)

            left = positions[(pos - 1) % len(positions)]
            right = positions[(pos + 1) % len(positions)]

            d1 = min(abs(i - left), n - abs(i - left))
            d2 = min(abs(i - right), n - abs(i - right))

            res.append(min(d1, d2))

        return res
