class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return all posible subsets from a given array.
        # either include the element or exclude it.
        # when index goes out of bounds, return the subset copy.

        res = []

        subset = []
        
        def dfs(i):
            # base condition: if the index goes out of bounds.
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # make a choice. add this element?
            subset.append(nums[i])
            dfs(i+1)

            # cleanup choice: remove this element.
            subset.pop()
            dfs(i+1)

        dfs(0) # start the backtracking at first index.

        return res
