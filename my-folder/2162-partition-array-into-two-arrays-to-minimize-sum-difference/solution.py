class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2

        # initial answer
        ans = abs(sum(nums[:N]) - sum(nums[N:]))

        # total
        total = sum(nums)
        half = total // 2 # half sum

        for k in range(1, N):
            left = [sum(comb) for comb in combinations(nums[:N], k)]
            right = [sum(comb) for comb in combinations(nums[N:], N-k)]

            right.sort() # for binary search

            for l in left:
                r = half - l
                i = bisect.bisect_left(right, r)

                if 0 <= i < len(right): # if index is valid
                    left_sum = l + right[i]
                    right_sum = total - left_sum

                    diff = abs(left_sum - right_sum)
                    ans = min(ans, diff)
        
        return ans
