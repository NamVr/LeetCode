class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float("inf")] * n for _ in range(n)] # n x n matrix

        # initialize matrix [i][i] = 0
        for i in range(n):
            dp[i][i] = 0
        
        # populate from given edges.
        for start, end, weight in edges:
            dp[start][end] = weight
            dp[end][start] = weight

        # run the O(V^3) loop i->k->j (k = inter.)
        # update distances for each intermediate.

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(
                        dp[i][j], dp[i][k] + dp[k][j]
                    )
        
        # now find the number of cities with threshold.
        # distance should be AT MOST threshold,
        # return N (city) with smallest number of cities (if tie = return the city with greatest number)
        min_reachable = n # tracks the sum() of every city (LOWEST)
        tie = -1 # for tie breaker, tracks the GREATEST number of the lowest city.

        for i in range(n):
            count = sum(
                1 for d in dp[i] if d <= distanceThreshold
            )
            
            # check for new minimum.
            if count <= min_reachable:
                min_reachable = count # unstable but works
                tie = i
        
        return tie
