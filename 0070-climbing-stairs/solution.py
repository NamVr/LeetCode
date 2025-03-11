class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 2 3 4 5 6 (value of n)
        # 1 2 3 5 8 13 (result)

        l,r = 1,1

        for i in range(n-1):
            temp = l
            l = l + r
            r = temp
        
        return l
