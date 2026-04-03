class Solution:
    def eraseOverlapIntervals(self, events: List[List[int]]) -> int:
        events.sort() # based on start time

        prev = float('-inf') # previous pointer
        res = 0

        for start, end in events:
            if start >= prev:
                # do nothing
                prev = end
                continue
            else:
                # if overlap is detected.
                # priority: smaller event
                res += 1
                prev = min(prev, end)
        
        return res
