class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # get O(n) total number of candies
        total = sum(candies)

        if total < k:
            # if total candies are less than the number of children, theres no equal division since some kid will be left hungry.
            return 0
        
        # run a binary search between 1 and total/k, the ideal max size of candy pile for each kid
        l, r = 1, total // k

        # we will store our final result as 0 initially
        res = 0

        while l <= r:
            m = (l + r) // 2

            # count will store number of piles for this iteration
            count = 0

            # run a linear check to see if this result is valid or not
            # check for each candy in the array, if you can make piles of value [mid]
            for c in candies:
                count += c // m

                # minor optimization, if anytime the count is above k, we can break the inner loop
                if count >= k:
                    break
            
            # check if count is valid or not (arithmetic check with k)
            if count >= k:
                # the result is valid
                res = m
                l = m+1
            else:
                # the result is not valid and search in lower half
                r = m-1
                

        return res
