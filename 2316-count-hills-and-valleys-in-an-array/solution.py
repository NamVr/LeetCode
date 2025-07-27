class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left = 0  # minimum than available constraint.
        res = 0
        
        for i in range(1, len(nums) - 1):
            # check if this is a hill or valley
            # if last recorded height is less/more than this and front height.
            if nums[i] != nums[i + 1]:
                if (nums[i] > nums[left] and nums[i] > nums[i + 1]) or (
                    nums[i] < nums[left] and nums[i] < nums[i + 1]
                ):
                    res += 1

                # if the next element is same, move the left pointer and continue.
                left = i

        return res

