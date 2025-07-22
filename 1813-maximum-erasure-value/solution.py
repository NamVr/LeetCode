class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # find the subarray with maximum sum that has unique elements
        # for example, 4,2,4,5,6 can have 2,4,5,6 unique subarray and 
        # 2+4+5+6 = 17 which is the answer. (contiguous sequence)

        res, curr = 0, 0 # constraints start with 1 <=
        seen = set() # create a set to track duplicated elements

        l = 0
        for r in range(len(nums)):
            while nums[r] in seen:
                curr -= nums[l]
                seen.remove(nums[l])
                l += 1
            
            curr += nums[r]
            seen.add(nums[r])
            res = max(res, curr)

        return res
