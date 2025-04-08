class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # given length of constraint is 100
        # we can create a array set to store elements upto 100
        seen = [False] * 101

        for i in reversed(range(len(nums))):
            if seen[nums[i]]: # is true,
                # remove all elements before i,
                # mathematically, we are removing in sets of 3
                # nums[0 .. i], at least i/3 + 1 removal operations are required
                return i // 3 + 1
            seen[nums[i]] = True
        
        return 0
