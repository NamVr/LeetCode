class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        while l <= r:
            m = (l + r) // 2
            total = 0

            for num in nums:
                total += (num + m - 1) // m
                if total > threshold:
                    break
                
            if total <= threshold:
                r = m - 1
            else:
                l = m + 1
        
        return l
