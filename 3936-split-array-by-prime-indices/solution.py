class Solution:
    def splitArray(self, nums: List[int]) -> int:
        # Edge case if number of elements are less than 2
        n = len(nums)
        if n < 2:
            return sum(nums) # O(1)

        # Sieve of Eratosthenes
        sieve = [True] * n # Space O(N), Time O(N)
        sieve[0] = sieve[1] = False

        A, B = [], [] # Space O(N)

        # run sieve algorithm
        i = 2
        while i*i < n: # O(logn)
            if sieve[i]: # is unmarked,
                for j in range(i*i, n, i): # O(logn)
                    sieve[j] = False
            i += 1
        
        # now split array based on sieve bool array
        for i, x in enumerate(sieve): # O(N)
            if x: # if true, the number is prime, put in array A
                A.append(nums[i])
            else:
                B.append(nums[i])

        return abs(sum(A) - sum(B)) # O(N)
        
