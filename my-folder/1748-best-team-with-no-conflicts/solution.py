class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = sorted(zip(scores, ages))
        n = len(pairs)

        dp = [pairs[i][0] for i in range(n)]

        for i in range(n):
            max_score, max_age = pairs[i]

            for j in range(i):
                score, age = pairs[j]

                # pick condition
                if max_age >= age:
                    dp[i] = max(
                        # current dp value (max upto i)
                        dp[i],

                        # picked item + ith max score
                        max_score + dp[j]
                    )
        
        return max(dp)
