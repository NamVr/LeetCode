class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        cnt = {} # hashmap

        for i in range(len(nums)):
            # i - nums[i] is the intuition
            diff = i - nums[i]

            # count previous positions with same difference
            c = cnt.get(diff, 0)

            res += i - c
            cnt[diff] = c + 1
            
        return res
