class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)

        max_f = max(c.values()) # get the maximum frequency count for each element

        # now extract all keys where values equals the max frequency
        arr = [i for i, freq in c.items() if freq == max_f]

        return max_f * len(arr)
