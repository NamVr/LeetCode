class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        n = len(intervals)

        dp = [0] * (n+1)

        for i in reversed(range(n)):
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            dp[i] = max(
                # skip this choice
                dp[i+1],
                # take this choice
                intervals[i][2] + dp[j]
            )
        
        return dp[0]
