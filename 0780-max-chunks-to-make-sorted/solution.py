class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        chunks = 0
        ps = 0 # prefix sum
        sps = 0 # sorted prefix sum

        for i in range(n):
            ps += arr[i]
            sps += i

            if ps == sps:
                chunks += 1
        
        return chunks

