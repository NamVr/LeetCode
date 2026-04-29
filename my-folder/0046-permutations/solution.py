class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n! permutations. can't skip any, it is all rearrangements.

        res = []

        def dfs(i):
            # base case.
            if i == len(nums):
                res.append(nums[:])
                return
            
            # pick:
            for j in range(i, len(nums)):
                # apply / swap
                nums[i], nums[j] = nums[j], nums[i]

                # backtrack
                dfs(i+1)

                # clean up / swap again
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0) # apply dfs i = 0th index.

        return res
