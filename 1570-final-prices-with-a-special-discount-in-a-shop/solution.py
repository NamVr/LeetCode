class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            # Look for first smaller or equal price that comes after current item
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    # Apply discount by subtracting prices[j] from current price
                    prices[i] = prices[i] - prices[j]
                    break

        return prices
