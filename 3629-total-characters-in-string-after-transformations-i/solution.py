class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7 # prime mod number to prevent integer overflows.
        cnt = [0] * 26 # counter for all letters in given string. (eg 2 As, 3 Bs..)

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1 

        # complete transformations 0 -> t times.
        for r in range(t):
            nxt = [0] * 26 # new counter for this 'r' transformation.
            nxt[0] = cnt[25] # put value of 'z' counts to new 'a' counts.
            nxt[1] = (cnt[25] + cnt[0]) % mod # put counts from 'a' and 'z' to b transformation.

            for i in range(2,26): # rest of the transformations.
                nxt[i] = cnt[i-1]
            cnt = nxt # old counter can now be discarded.
        
        return sum(cnt) % mod
