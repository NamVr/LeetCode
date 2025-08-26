class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # n-k+1
        l = 0

        q = deque() # monotonic nature, maximum element at front.

        for r in range(len(nums)):
            # while queue has elements and the last added element is less than the current [r] element.
            # monotonic decreasing nature is violated.
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            # then we will append the new element index.
            # if the element is lesser or equal, then monotonicity is maintained
            # lesser elements can be added to queue.
            q.append(r)

            # if the index of left element is more than the index of the first element inserted,
            # that means, the sliding window must be shifted further.
            if l > q[0]:
                q.popleft()

            # we can only maintain a window when k elements are maintained.
            # then only, result can be added.
            # due to the decreasing nature of the dq, the first element is the maximum
            if (r + 1) >= k:
                res.append(nums[q[0]])

                # the sliding window is shifted.
                l += 1
        
        return res

            

