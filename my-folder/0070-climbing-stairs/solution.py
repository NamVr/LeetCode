class Solution:
    memo = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        self.memo[1] = 1
        self.memo[2] = 2
        
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.memo[n]
