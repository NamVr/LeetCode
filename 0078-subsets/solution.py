class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # represents the current subset.
        subset = []

        # this function will take decision for the given INDEX passed.
        def dfs(i):
            if i >= len(nums): # out of bounds, return base case.
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision to not include nums[i]
            subset.pop() # remove the added append from previous recursive call.
            dfs(i+1)

        # call the function from base index 0
        dfs(0)

        return res
