class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # what kind of question is this lol?
        res = []
        n = len(s)

        i = 0 # starting index of each group?

        while i < n:
            res.append(s[i : i + k]) # slices from index [i to i + k) 
            i += k # hops K times over for next group.
        
        # fill the last group. (only need to fill k-occupied positions)
        res[-1] += fill * (k - len(res[-1]))

        return res
