class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))

        score = 0

        for num, idx in sorted_nums:
            if nums[idx] != -1: # not marked
                score += num
                nums[idx] = -1 # mark it now

                if idx > 0: #left
                    nums[idx-1] = -1
                if idx < n-1: #right
                    nums[idx+1] = -1

        return score
