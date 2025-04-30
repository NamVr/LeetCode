class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if int(math.floor(math.log10(num)) + 1) % 2 == 0:
                res += 1

        return res
