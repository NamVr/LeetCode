class Solution:
    def findRepeatedDnaSequences(self, s):
        n = len(s)

        # create a hashmap of int
        m = set() # dna str -> int
        res = set()

        for i in range(n - 9): # 0 .. n-10
            # get the current strand of the dna, i .. i + 10
            dna = s[i:i+10]

            # add it to the hashmap, a repeated string.
            # if its more than once, then add to the result.

            if dna in m:
                res.add(dna)
            else:
                m.add(dna)

        return list(res)
