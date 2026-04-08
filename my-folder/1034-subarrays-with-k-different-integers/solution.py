class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            counter = defaultdict(int)

            res = 0
            l = 0

            for r in range(len(nums)):
                counter[nums[r]] += 1

                while len(counter) > k:
                    # shift
                    counter[nums[l]] -= 1
                    if counter[nums[l]] == 0:
                        del counter[nums[l]]
                    l += 1
                
                res += r-l+1

            return res
        
        return helper(k) - helper(k-1)  
