class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0

        # case 1 : fix left
        for r in reversed(range(n)):
            if colors[r] != colors[0]:
                res = max(res, r)
                break
        
        # case 2: fix right
        for l in range(n):
            if colors[l] != colors[n-1]:
                res = max(res, n-1-l)
                break
        
        return res
