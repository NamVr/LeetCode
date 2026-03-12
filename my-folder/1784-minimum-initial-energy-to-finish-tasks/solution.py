class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # we need to finish all tasks with minimum initial energy.
        # is GUARANTEED to finish all tasks.
        # apply MAXIMUM energy based binary search till we find a minimum.

        # MAX : 10**5 which means O(N LOG N) is also accepted, we just need a sorting logic, ordering doesn't matter after.
        # either binary search or sorting.

        # sort: minimum - actual as per the flow.
        # eg: 10 minimum required and 5 consumption, then 10-5 = 5.

        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)  # O(N LOG N)

        curr = 0 # the actual energy consumed (for tracking last element's energy)
        res = 0 # the minimum initial energy (which will be build up with last consumed + minimum of this point)

        for actual, minimum in tasks: # sorted tasks
            res = max(res, minimum + curr) # to minimize
            curr += actual # in the end, it equals sum(minimum energy at each step)
        
        return res
