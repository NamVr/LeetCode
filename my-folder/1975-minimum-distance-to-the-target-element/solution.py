class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        m = float("inf")
        for i, x in enumerate(nums):
            if x == target:
                m = min(m, abs(i-start))

        return m
