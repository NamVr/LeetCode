class Solution:
    def eraseOverlapIntervals(self, events: List[List[int]]) -> int:
        res = 0

        events.sort() # [start,end] sorted based on start indexes.
        endTime = events[0][1] # keep track of the latest end value, start with the first index.

        for start, end in events[1:]:
            # ground truth, if the start value of the current element is less than the end time
            # that will result in an overlap.

            if start >= endTime:
                # normal condition, update endTime
                endTime = end # new end
            else:
                # overlap detected.
                res += 1
                endTime = min(end, endTime) # it is better to keep the end time minimum to get less overlaps (greedy)
        return res
