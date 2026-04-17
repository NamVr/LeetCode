class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        m = {}
        res = float('inf')

        for i, x in enumerate(nums):
            if x in m:
                res = min(res, i - m[x])
            
            m[int(str(x)[::-1])] = i # store the reverse in hashmap

        return res if res != float('inf') else -1
