class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        # create a hashmap to map each element to its coordinate.
        # traverse the matrix to complete this hashmap.
        mat_to_position = {} # hashmap for each element in grid
        for r in range(ROWS):
            for c in range(COLS):
                mat_to_position[mat[r][c]] = (r,c) # tuple cords

        # store row and column count
        row = [0] * ROWS
        col = [0] * COLS

        # traverse the arr to mark visited
        for i in range(len(arr)):
            r,c = mat_to_position[arr[i]]
            # mark if that row/col has a new visited element
            row[r] += 1
            col[c] += 1

            # lastly check if any row is filled.
            if row[r] == COLS or col[c] == ROWS:
                return i # return iteration step count


