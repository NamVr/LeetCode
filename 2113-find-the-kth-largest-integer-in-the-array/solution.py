class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        n = len(nums)

        for i in range(k):
            heappush(heap, int(nums[i]))

        for i in range(k,n):
            if int(nums[i]) > heap[0]:
                heappushpop(heap, int(nums[i]))
        
        return str(heap[0])
