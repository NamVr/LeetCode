class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1): # O(N) time
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0
        
        # after performing all operations, shift all 0s to the end of the array
        k = 0 # non zero index

        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        
        while k < n:
            nums[k] = 0 # fill remaining positions with non zero index
            k += 1 

        return nums # O(1) in place
