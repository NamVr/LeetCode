class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # create a result array
        n = len(nums)
        res = [0] * n

        l,r = 0, n-1

        # zip tuple iterator, zips n + start: n-1, stop: -1, step: -1
        for i, j in zip(range(n), range(n - 1, -1, -1)):
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1
            
            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1
            
        # fill the remaining pivot elements
        while l <= r:
            res[l] = pivot
            l += 1
        
        return res
