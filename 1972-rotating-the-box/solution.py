class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])

        for r in range(ROWS):
            i = COLS- 1 # transpose counter
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1 # shift to left
                elif box[r][c] == "*":
                    i = c-1
        

        # rotate the box
        res = []

        for c in range(COLS):
            col = [] # this is row after rotation
            for r in reversed(range(ROWS)):
                col.append(box[r][c])
            
            res.append(col)

        return res

