class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Max Constraint: 1 ... 10**9
        l, r = 1, 10**9

        while l < r:
            m = (l + r) // 2 # max number of balls in current bag
            count = 0

            for i in nums: # the ith bag contains i balls.
                # find count of operations needed if every bag has <= m balls
                count += (i-1) // m # penalty is minimized: i-1 / mid (binary search)

            if count > maxOperations: # try lesser
                l = m + 1
            else:
                r = m
        
        # l is guaranteed to be the answer
        return l
