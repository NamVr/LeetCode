class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        # n : min cost

        def dp(i):
            # base case:
            if i in [0,1]:
                return 0
            
            if i in memo:
                return memo[i]
            
            # Calculate cost if taking 1 step (from i-1)
            # dp(i-1) is cost to reach position i-1, then add cost to step on stair i-1
            cost_from_prev_step = dp(i - 1) + cost[i - 1] 
            
            # Calculate cost if taking 2 steps (from i-2)
            # dp(i-2) is cost to reach position i-2, then add cost to step on stair i-2
            cost_from_two_steps_back = dp(i - 2) + cost[i - 2]
            
            # The minimum cost to reach 'position i' is the minimum of these two options
            memo[i] = min(cost_from_prev_step, cost_from_two_steps_back)
            return memo[i]
        
        return dp(n)
