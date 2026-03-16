class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(m) - 1

        while l < r:
            for i in range(r-l): # per rotation.
                t, b = l, r
                temp = m[t][l + i] # one extra variable.

                # make all r-l rotation.
                m[t][l + i] = m[b - i][l]
                m[b - i][l] = m[b][r - i]
                m[b][r - i] = m[t + i][r]
                m[t + i][r] = temp
                # layer complete.
            
            l += 1
            r -= 1
