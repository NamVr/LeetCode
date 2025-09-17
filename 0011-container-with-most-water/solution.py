class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # AREA = L * B where 
            # L = length of container (r-l) Index.
            # B = the most minimum height from both sides of the container.
            temp = (r-l) * min(height[l], height[r])
            res = max(res,temp)

            # proceed while keeping the maximum height.
            # for example, if left tower is higher than the right,
            # then calculate area for the next right tower (r--)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return res
