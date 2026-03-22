class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # in-place rotate using 4 pointers.
        # rotate 4 times and check if they match.
        n = len(mat) # n x n given.

        for k in range(4): # per 90 degree rotation.
            l, r = 0, n-1

            while l < r:
                for i in range(r-l): # per rotation
                    t, b = l, r
                    temp = mat[t][l+i] # top left.

                    mat[t][l + i] = mat[b - i][l]
                    mat[b - i][l] = mat[b][r - i]
                    mat[b][r - i] = mat[t + i][r]
                    mat[t + i][r] = temp
                
                # after all rotations at first layer.
                l += 1
                r -= 1
                
            if mat == target:
                return True
        
        return False
