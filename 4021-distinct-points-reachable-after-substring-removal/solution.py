class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        n = len(s)

        # we have to remove 'k' window subarray string
        # add all possible string combinations to a set
        # sort those possible combinations since sorting = same distinct destination
        # return the distinct result

        # to avoid TLE, using total - prefix sum
        # prefix[i] is the net from start to i-1
        p = [(0,0)]

        for c in s:
            dx, dy = dirs[c]
            x, y = p[-1]
            p.append((x+dx, y+dy))

        # extract the prefix.
        t_x, t_y = p[-1]

        st = set()
        # generate all strings after removing 'k' substring
        for i in range(n-k+1):
            x1, y1 = p[i+k]
            x, y = p[i]

            # final = total - prefix[i+k] - prefix[i]
            st.add((t_x - (x1 - x) , (t_y - (y1 - y))))
            #rm = s[:i] + s[i+k:]
            #x, y = 0, 0 # start point.

            #for c in rm: # for every character in remaining string
            #    dx, dy = dirs[c]
            #    x += dx
            #    y += dy

            #st.add((x,y))
            #st.add("".join(sorted(rm)))

        # sorting worked for most cases. failed at
        # "DURLU" , 2
        # "RLU" → "LRU"
        # "DUU" → "DUU" 
        # both end at 0,1 which is why it failed.
        # lets add last check to all these strings.

        return len(st)
