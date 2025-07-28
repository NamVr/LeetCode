class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        # median is the middle element in non decreasing order.
        # so first of all, sort the array in ascending order.
        nums.sort() # O(nlogn) time

        for i in range(n//3, n, 2):
            # to maximize median, pair last two elements and first element.
            res += nums[i]

        return res
