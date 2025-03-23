class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort() # start,end : sort based on starting point
        prev = intervals[0][1] # keep track of last end point

        # traverse through all intervals from the second element
        for start, end in intervals[1:]:
            if prev <= start:
                # non overlapping, update the new end
                prev = end
            else:
                # overlapping
                res += 1
                prev = min(prev,end)

        return res
