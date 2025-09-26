class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 2 sides of the triangle must be greater than the third.
        # pick three numbers a, b, c where
        # all these 3 conditions satisfy:
        # 1. a + b > c
        # 2. b + c > a
        # 3. c + a > b

        # Brute force will be O(n^3) which is NOT optimal.
        res = 0
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()

        for i in range(n - 2):
            if nums[i] == 0:
                continue

            k = i + 2
            for j in range(i+1, n-1):
                k = max(k, j+1)
                
                while (k < n and nums[i] + nums[j] > nums[k]):
                    k+=1
                
                res += (k-j-1)

        return res
