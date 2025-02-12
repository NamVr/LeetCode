class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        max_arr = [0] * 82 # or a hashmap for storage
        # 82 is a precomputational result storage instead of a hashmap
        # based on the given constraints

        for i in nums:
            s = sum(int(d) for d in str(i)) # find sum of digits using string technique
            if max_arr[s] != 0:
                res = max(res, i + max_arr[s]) # find the max
            max_arr[s] = max(max_arr[s], i)

        return res
