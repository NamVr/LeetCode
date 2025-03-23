class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP bottom up approach, max = amount + 1 or infinity
        dp = [amount + 1] * (amount + 1) # range is 0 (no coins upto amount)
        dp[0] = 0 # base case, for amount 0, 0 coins are needed

        # a = amount from 1 upto amount + 1
        for a in range(1, amount + 1):
            # c = no of coin demoninations given
            for c in coins:
                # check if the coin value exceeds the current amount
                if a - c >= 0:
                    # take the minimum of current value and this coin + amount - coin
                    dp[a] = min(dp[a], dp[a-c] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
