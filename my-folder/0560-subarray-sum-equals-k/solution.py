class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        count[0] = 1

        curr = 0

        for num in nums:
            curr += num
            res += count[curr - k]

            # update storage prefix -> count
            count[curr] += 1   

        return res
