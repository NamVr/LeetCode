class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [0] * n

        res[0] = cost[0]
        res[1] = cost[1]

        for i in range(2,n):
            res[i] = min(res[i-1], res[i-2]) + cost[i]
        
        return min(res[-1], res[-2])
