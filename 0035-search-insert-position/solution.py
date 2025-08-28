class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # insert when,
        # if m == target OR
        # the element at which target is less, eg 2

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r -= 1
            else:
                l += 1
        
        return l # lower bond
