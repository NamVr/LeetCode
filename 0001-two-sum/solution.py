class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in m:
                return [i, m[diff]]

            m[n] = i # add it to the hashmap
