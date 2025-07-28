class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for i in nums:
            max_or |= i
        
        res = 0

        # define the backtracking template.
        def backtrack(i, curr):
            nonlocal res

            # base case
            if i == len(nums):
                if curr == max_or: # if current OR is the max or, it is a valid subset.
                    res += 1
                return
            
            # recursive call.
            # 1. make a decision,
            backtrack(i+1, curr | nums[i])

            # 2. revert the decision and move on.
            backtrack(i+1, curr)
        
        # run the backtracking.
        backtrack(0,0)

        return res
