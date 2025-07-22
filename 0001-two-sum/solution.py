class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # number : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in m:
                return [i, m[diff]]
            
            m[num] = i
