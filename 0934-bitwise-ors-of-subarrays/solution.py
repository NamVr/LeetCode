class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()

        cur = {0}

        for x in arr:
            cur = { x | y for y in cur } | { x }
            res |= cur
        return len(res)
