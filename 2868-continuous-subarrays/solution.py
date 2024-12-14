class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
        n = len(nums)

        freq = {} # map

        while r < n:
            # map.get(index, default_value = 0)
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            # shrink window from left
            while max(freq) - min(freq) > 2:
                # if it is not continuous, remove left element
                freq[nums[l]] -= 1 # from the map, removed

                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1 # l++; while loop increment
            
            # add count of all valid subarrays
            res += r - l + 1
            r += 1 # r++; while loop increment

        return res
