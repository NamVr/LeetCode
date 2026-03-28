class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        res = 0 # find max water area
        # Area = (r-l) * min(h[r],h[l])

        while l < r:
            area = (r-l) * min(height[r], height[l])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
