class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Create a Min-Heap.
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        # We don't care for values more than K elements.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Simply add the element, and remove excess elements if more than k elements.
        heapq.heappush(self.minHeap, val)

        # use the while function technically, but given k elements is guaranteed, IF statemenet is also OK.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # return the kth largest element in stream.
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
