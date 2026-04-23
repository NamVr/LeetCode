class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # number -> their indexes.

        m = defaultdict(list)
        n = len(nums)

        for i, num in enumerate(nums):
            m[num].append(i)

        res = [0] * n

        # process each group individually.
        for group in m.values():
            total = sum(group)
            k = len(group)
            prefix = 0

            for count_left, idx in enumerate(group):
                # j is the count of elements in left of the group
                # left contribution
                left = count_left * idx - prefix
                
                # right contribution
                count_right = k - count_left - 1 # k elements total, at jth position, we have k-j-1 elements to the right
                sum_right = total - prefix - idx
                right = sum_right - count_right * idx
                
                res[idx] = left + right
                
                prefix += idx

        return res
