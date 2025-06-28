class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        vals = [ [i, nums[i]] for i in range(n)] # value - index mapping

        vals.sort(key=lambda s: -s[1]) # descending order

        vals = sorted(vals[:k]) # sort first k elements by index order

        return [val for i, val in vals]
        
