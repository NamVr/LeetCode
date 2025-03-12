class Solution:
    def lower_bound(self, nums):
        i = len(nums)
        l, r = 0, i - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] < 0:
                # then positive number is higher
                l = m+1
            else:
                r = m-1
                i = m
        
        return i
    
    def upper_bound(self,nums):
        i = len(nums)
        l, r = 0, i-1

        while l <= r:
            m = (l+r) // 2

            if nums[m] <= 0:
                l = m+1
            else:
                r = m-1
                i = m
        
        return i
    
    def maximumCount(self, nums: List[int]) -> int:
        # -2,-1,-1, 1, 2, 3, 4, 5 (8 elements) mid is 8-0/2 = 4
        # arr[4] = 2, which is not zero. we have to find zero
        # 2 > 0, we will reduce the search half to the lower half (r = m-1)
        # 4 elements: -2,-1,-1, 1 | m = (4-0)/2 = 2
        # arr[2] = -1 which is less than zero, | l = m+1 => 3 (only element left)
        # arr[3] = 1 which is greater than zero, we've found the middle point

        # Actual Solution:
        # max(pos,neg) = max(5, 3) = 5
        # number of binary search iterations = 3

        # all int from first non zero to last will be positive
        pos = len(nums) - self.upper_bound(nums)

        # all int from index 0 to first zero index will be negative
        neg = self.lower_bound(nums)

        return max(pos,neg)
