class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        l = 0
        res = 0

        for r in range(1, n+k-1):
            # check if r and r-1 is the same color
            # then left pointer jumps to r pointer
            if colors[r % n] == colors[(r-1) % n]:
                l = r
            
            # check if window size is more than k
            # window size is calculated using r-l + 1
            # (0,1) means 1-0 + 1 = 2 window size
            if r-l+1 > k:
                l+=1
            
            # check if window size is exactly k
            if r-l+1 == k:
                res += 1
        
        return res
