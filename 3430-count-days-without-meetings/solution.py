class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # sort the meetings based on start key
        meetings.sort() # O(nlogn)

        prev = 0 # since days starts from 1

        for start,end in meetings:
            # start point is the max of prev end + 1 OR current start
            start = max(start, prev + 1)
            length = end - start + 1 # handle inclusive condition
            days -= max(length, 0) # handle negative cases
            prev = max(end, prev) # end is the max of prev end or curr end

        # return the remaining number of days
        return days
