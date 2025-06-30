class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m = Counter(nums) # O(n)
        res = 0

        for num in m:
            if num + 1 in m:
                cur = m[num] + m[num+1]
                res = max(cur,res)

        return res
