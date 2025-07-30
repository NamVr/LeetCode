class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n # flights 1 -- n

        # Brute Force: TLE
        # for first, last, seats in bookings:
        #     for i in range(first-1, last):
        #         res[i] += seats

        # Solve using Difference Array - Line Sweep Algorithm
        # 1. Simple array [0] *n
        # 2. Mark +x on the "first" element.
        # 3. Mark -x on the "last+1" element. (if last element, ignore this step)
        # 4. Finally create a prefix array on the above resultant array (difference array)

        for first, last, seats in bookings:
            res[first-1] += seats

            if last < n:
                res[last] -= seats

        return list(accumulate(res))
