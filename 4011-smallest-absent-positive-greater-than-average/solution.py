class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        avg = sum(nums) / n

        s = set(nums)

        for i in range(int(avg) + 1, 102):
            if i not in s and i > 0:
                return i
