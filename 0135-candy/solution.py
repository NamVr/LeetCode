class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = 0

        candies = [1] * n # minimum 1 candy per person

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in reversed(range(1, n)):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i] + 1, candies[i-1])
            res += candies[i-1]
        
        return res + candies[n-1]
