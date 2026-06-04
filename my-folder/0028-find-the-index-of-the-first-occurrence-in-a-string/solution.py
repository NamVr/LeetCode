class Solution:
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        n, p = len(haystack), len(needle)
        for l in range(n):
            if haystack[l:l+p] == needle:
                return l
