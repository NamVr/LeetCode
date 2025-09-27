class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # stairs 0 .. n (n+1 total)
        dp = [float("inf")] * (n+1)
        # cost of each step is given (n length)

        # from each step, you can only jump to i+1, i+2 or i+3
        # cost of jumping from i to j is 
        # cost[j] + (j-i)^2

        # DP problem. each step minimize the cost to reach next step.
        # start point: dp[0] = 0
        dp[0] = 0
        # dp[j] = min cost to reach j

        for j in range(1, n+1): # 1st indexed array
            for s in [1,2,3]: # minimum ways to reach j is j-1, j-2 and j-3 (3 steps)
                i = j - s # (previous step)

                if i >= 0: # impossible condition
                    # minimize the cost.
                    dp[j] = min(
                        dp[j], # previous step input
                        dp[i] + costs[j-1] + (j-i)**2 # this step cost calculation
                    )

        return dp[n]
