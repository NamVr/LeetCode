class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        res = [0] * 1001 # ? get max distance from constraints.
        
        for seats, start, end in trips:
            # Difference Array. +x at start, -x at end+1 (optional) -> prefix array using list(accumulate(arr))
            res[start] += seats
            res[end] -= seats # dropped at end means end is not included.

        # At any point, if seats > capacity, return False.
        res = list(accumulate(res))

        for i in res:
            if i > capacity:
                return False

        return True
