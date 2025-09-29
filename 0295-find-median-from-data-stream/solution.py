class MedianFinder:
    def __init__(self):
        # small heap is larger always by 1.
        self.small = [] # max heap
        self.large = [] # min heap
        # self.n = 0  # to find the middle value
        # odd: arr[n//2 + 1]
        # even: 1/2 (arr[n // 2] + arr[n // 2 + 1])
        # self.median = 0 # initially.

    def addNum(self, num: int) -> None:
        heappush(self.small, -num) # O(logn) to push new element.

        # Balance both heaps. IF small's largest > largest small, swap.
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large, val)

        # Balance size. Small must be equal or greater by 1 than large.
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        
        # if large is too large (large > small is impossible)
        if len(self.large) > len(self.small):
            val = heappop(self.large)
            heappush(self.small, -val)

        # calculate the median
        #if self.n & 1: # odd
        #    self.median = self.heap[self.n // 2]
        #else: # even
        #    self.median = (self.heap[self.n // 2] + self.heap[self.n // 2 - 1]) / 2

    def findMedian(self) -> float:
        # EVEN - both heaps are of same size.
        # ODD - small is +1 than large, return that.

        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
