class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Lets code up brute force solution first then add caching.
        # Now let's add caching.

        cache = [0] * len(questions) # as per given constraints, points less than 1 are not possible

        # define a helper function that takes the index of the questions
        # returns the points or the reward of that index and further
        def helper(i):
            # base case, if i is out of bounds
            if i >= len(questions):
                return 0

            # to avoid TLE, check if this is in cache. (Top-down approach DP)
            if cache[i]:
                return cache[i]
            
            # now we have to take the max of either choosing or skipping.
            # choose: run backtrack on this + next element after penalty + add current points/reward
            # skip: run backtrack on the next element - dont add reward since skipped

            # unpack the points and brainpower from the index
            points, brainpower = questions[i]

            cache[i] = max(
                helper(i + 1), # skip
                points + helper(i + 1 + brainpower)
            )

            # need to store this result in caching
            return cache[i]
        
        return helper(0)
