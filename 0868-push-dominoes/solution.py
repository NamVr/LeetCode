class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # string is immutable, convert to a list
        res = list(dominoes)

        # exploratory queue, add all L and R elements in it.
        q = deque()
        for i,d in enumerate(res):
            if d != ".":
                q.append((i,d)) # tuple (index, data: "L" | "R" | ".")
        
        # run the exploration.
        while q:
            # extract tuple values
            i, d = q.popleft()

            # L Case: Check if in bounds and previous element.
            if d == "L" and i > 0 and res[i-1] == ".":
                q.append((i-1,"L")) # add to exploration for next second.
                res[i-1] = "L" # tilt the previous element after 1s.

            # R Case: Check if in bounds and next element.
            elif d == "R" and i + 1 < len(res) and res[i+1] == ".":
                # internal check: if next to next element is R (sandwitch effect) and in bounds.
                if i + 2 < len(res) and res[i+2] == "L":
                    q.popleft() # then remove that "L" from queue too, dont explore it.
                else:
                    q.append((i+1, "R")) # normally explore the R for next second.
                    res[i+1] = "R" # tilt the next element after 1s.
        
        # AFTER all exploration
        return "".join(res)

