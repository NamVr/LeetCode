class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = [False] * len(queries)

        prefix = [0] * len(nums)
        prefix[0] = 0

        # create a prefix violation array and run through queries end-start == 0 means no error

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                # violation found
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
        
        # now test for queries
        
        for i, (start, end) in enumerate(queries):
            res[i] = prefix[end] - prefix[start] == 0


        return res
