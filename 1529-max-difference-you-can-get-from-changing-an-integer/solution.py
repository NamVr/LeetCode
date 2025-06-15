class Solution:
    def maxDiff(self, num: int) -> int:

        def swap(x,y):
            return str(num).replace(str(x), str(y)) # change all x to y in num.
       
        mi = ma = num

        for x in range(10):
            for y in range(10):
                res = swap(x,y) # this is a string!

                # leading zeros check
                if res[0] != "0":
                    mi = min(mi, int(res))
                    ma = max(ma, int(res))
                
        return ma - mi
