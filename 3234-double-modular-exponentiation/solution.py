class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []

        def helper(a,b,c,m):
            ans = 1
            a = a % 10

            # if odd, a * (a^ b/2) ^ 2
            # if even, (a^ b/2) ^ 2

            while b > 0:
                if b & 1:
                    ans = (ans * a) % 10
                
                a = (a*a) % 10
                b = b >> 1
            
            a = ans
            ans = 1

            while c > 0:
                if c & 1:
                    ans = (ans * a) % m
                
                a = (a*a) % m
                c = c >> 1
            
            return ans

        for i in range(len(variables)):
            a, b, c, m = variables[i]

            if helper(a,b,c,m) == target:
                res.append(i)

        return res
