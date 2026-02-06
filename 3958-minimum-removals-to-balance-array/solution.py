class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # balanced if max(val) <= k * min(val)
        n = len(nums)

        # we have to remove minimum no. of elements. (can't make it empty)
        nums.sort() # now array is sorted.

        res = n
        r = 0

        for l in range(n):
            while r < n and nums[r] <= nums[l] * k:
                r += 1
            
            res = min(res, n-(r-l))
        
        return res
